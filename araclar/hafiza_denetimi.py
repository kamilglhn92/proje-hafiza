#!/usr/bin/env python3
"""Hafıza denetimi: token harcamadan yapının sağlığını kontrol eder.

Kullanım:  python araclar/hafiza_denetimi.py [--kok KLASOR]
Yalnız Python standart kütüphanesini kullanır; kurulum gerektirmez.
Hiçbir dosyayı değiştirmez, yalnız rapor yazar. Claude, bakım sırasında
yalnız bu raporun işaret ettiği dosyaları açar.
"""

import argparse
import re
import sys
from pathlib import Path

CATI = "CATI-HAFIZA"
SABLON = "_SABLON"
ATLANAN = {CATI, SABLON, "araclar"}
SATIR_SINIRI = 150
KOK_CLAUDE_SINIRI = 200
ACIK_IS_SINIRI = 15
KAYNAK_KLASORLERI = ("belgeler", "veriler", "gorseller", "ses-ve-video")
KAPALI_DURUMLAR = ("tamamlandı", "tamamlandi", "iptal")

ATIF = re.compile(r"`([^`\n]+)`")


def oku(yol):
    try:
        return yol.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def satir_sayisi(yol):
    return oku(yol).count("\n") + 1


def atiflar(metin):
    """Ters tırnak içindeki dosya/klasör adlarını döndürür."""
    return {a.strip() for a in ATIF.findall(metin)}


def departman_klasorleri(kok):
    return sorted(
        p for p in kok.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.name not in ATLANAN
    )


def harita_kontrolu(klasor, bulgular, etiket, kok):
    """Klasördeki .md dosyaları ile README.md haritasını karşılaştırır."""
    harita = klasor / "README.md"
    if not harita.exists():
        bulgular.append(f"[harita yok] {etiket}/README.md bulunamadı")
        return
    adlar = atiflar(oku(harita))
    for md in sorted(klasor.glob("*.md")):
        if md.name == "README.md":
            continue
        if md.name not in adlar and not any(a.endswith("/" + md.name) for a in adlar):
            bulgular.append(f"[haritada yok] {etiket}/{md.name}")
    for ad in sorted(adlar):
        if (ad.endswith(".md") and "/" not in ad
                and not (klasor / ad).exists() and not (kok / ad).exists()):
            bulgular.append(f"[dosya yok] {etiket}/README.md '{ad}' gösteriyor ama dosya yok")


def kaynak_kontrolu(context, bulgular, etiket):
    kaynaklar = context / "kaynaklar"
    indeks = kaynaklar / "kaynak-indeksi.md"
    if not kaynaklar.is_dir():
        return
    metin = oku(indeks)
    for alt in KAYNAK_KLASORLERI:
        klasor = kaynaklar / alt
        if not klasor.is_dir():
            continue
        for dosya in sorted(klasor.iterdir()):
            if dosya.is_file() and dosya.name != ".gitkeep" and dosya.name not in metin:
                bulgular.append(f"[indekste yok] {etiket}/kaynaklar/{alt}/{dosya.name}")


def sisme_kontrolu(dosyalar, kok, bulgular):
    for yol in dosyalar:
        sinir = KOK_CLAUDE_SINIRI if yol == kok / "CLAUDE.md" else SATIR_SINIRI
        n = satir_sayisi(yol)
        if n > sinir:
            bulgular.append(f"[şişmiş] {yol.relative_to(kok).as_posix()}: {n} satır (sınır {sinir}) → özetle, ayrıntıyı arşive taşı")


def is_defteri_kontrolu(cati, bulgular):
    defter = cati / "is-defteri.md"
    arsiv = cati / "is-defteri-arsiv.md"
    if not defter.exists():
        bulgular.append(f"[dosya yok] {CATI}/is-defteri.md")
        return
    satirlar = [s for s in oku(defter).splitlines() if re.match(r"^\|\s*\d{3}\s*\|", s)]
    kapali = [s for s in satirlar if any(d in s.lower() for d in KAPALI_DURUMLAR)
              and "devam" not in s.lower()]
    if kapali:
        bulgular.append(f"[arşive taşı] is-defteri.md içinde kapanmış {len(kapali)} iş var")
    if len(satirlar) > ACIK_IS_SINIRI:
        bulgular.append(f"[uzun] is-defteri.md'de {len(satirlar)} açık iş var (sınır {ACIK_IS_SINIRI})")
    numaralar = [int(n) for n in re.findall(r"^\|\s*(\d{3})\s*\|", oku(defter) + "\n" + oku(arsiv), re.M)]
    son = re.search(r"Son verilen iş no:\s*\**(\d{3})", oku(defter))
    if numaralar and son and int(son.group(1)) < max(numaralar):
        bulgular.append(f"[numara] 'Son verilen iş no' {son.group(1)}, ama kullanılan en büyük numara {max(numaralar):03d}")
    return len(satirlar)


def main():
    ap = argparse.ArgumentParser(description="Hafıza denetimi")
    ap.add_argument("--kok", default=str(Path(__file__).resolve().parent.parent),
                    help="Kurum klasörü (varsayılan: bu betiğin bir üst klasörü)")
    kok = Path(ap.parse_args().kok).resolve()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    cati = kok / CATI
    bulgular = []
    if not cati.is_dir():
        print(f"{CATI} klasörü bulunamadı: {kok}")
        return 1

    if "KURULUM: BEKLIYOR" in oku(cati / "kimlik.md"):
        bulgular.append("[kurulum] Sistem henüz kurulmamış → 'kurulum' becerisini çalıştır")

    harita_kontrolu(cati, bulgular, CATI, kok)

    sicil = oku(cati / "departmanlar.md")
    sicil_adlari = {a.rstrip("/") for a in atiflar(sicil) if a.endswith("/")}
    olcum = [kok / "CLAUDE.md"] + sorted(cati.glob("*.md"))

    departmanlar = departman_klasorleri(kok)
    for d in departmanlar:
        if d.name not in sicil_adlari:
            bulgular.append(f"[sicilde yok] {d.name}/ → incele ve departmanlar.md'ye işle")
        claude = d / "CLAUDE.md"
        if not claude.exists():
            bulgular.append(f"[talimat yok] {d.name}/CLAUDE.md bulunamadı")
        else:
            olcum.append(claude)
        context = d / "context"
        if context.is_dir():
            harita_kontrolu(context, bulgular, f"{d.name}/context", kok)
            kaynak_kontrolu(context, bulgular, f"{d.name}/context")
            olcum += sorted(context.glob("*.md"))
    for ad in sorted(sicil_adlari - {d.name for d in departmanlar} - ATLANAN):
        if not (kok / ad).exists():
            bulgular.append(f"[klasör yok] departmanlar.md '{ad}/' gösteriyor ama klasör yok")

    sisme_kontrolu([p for p in olcum if p.exists()], kok, bulgular)
    acik = is_defteri_kontrolu(cati, bulgular)

    print(f"Hafıza denetimi · {kok.name}")
    print(f"Departman: {len(departmanlar)} · açık iş: {acik if acik is not None else '?'}")
    if not bulgular:
        print("Sorun bulunmadı.")
    else:
        print(f"{len(bulgular)} bulgu:")
        for b in bulgular:
            print("  - " + b)
    return 0


if __name__ == "__main__":
    sys.exit(main())
