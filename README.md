# Proje Hafızası

**Claude Code için kendi kendini kuran çalışma ekosistemi.** Bir klasöre koyarsınız, Claude'u orada açarsınız; birkaç soruyla kurulur, siz çalıştıkça kendisi büyür.

*English summary below.*

---

## Neden?

Claude ile uzun süre çalışan herkes aynı iki sorunu yaşar:

1. **Bağlam kopması.** Her yeni sohbette proje baştan anlatılır; dün alınan karar bugün unutulur.
2. **Token israfı.** Her şey her seferinde yeniden okunur, yeniden açıklanır.

Proje Hafızası bu iki sorunu sade bir **kurum** benzetmesiyle çözer:

| Gerçek hayatta | Bu sistemde |
|---|---|
| Kurum | `Projeler` klasörünüz |
| Departmanlar | Alt klasörler: her proje veya iş alanı |
| Genel Müdür | Claude: işi alır, doğru departmana yönlendirir, hafızayı tutar |
| Personel | Alt ajanlar: araştırmacı, denetçi (gerektikçe yenileri) |
| Arşiv | `CATI-HAFIZA/`: kurumun ortak hafızası |
| Siz | Kurumun sahibi: kararları verir, gerçek dünyadaki işleri yaparsınız |

## Nasıl çalışır?

1. **İlk çalıştırma:** Claude kurulumun yapılmadığını görür ve 6 kısa soru sorar (kimsiniz, ne iş yaparsınız, hangi tür işleriniz var, nasıl yanıt istersiniz…). Cevaplarla ortak hafızayı doldurur.
2. **Çalıştıkça:** Yeni bir iş verdiğinizde Claude nereye ait olduğuna kendisi karar verir. Gerekirse yeni bir departman (klasör) açar, hafızasını kurar, iş defterine yazar. Size yalnız sizin bilebileceğiniz şeyleri sorar.
3. **Her oturumda:** Claude önce kısa bir haritayı ve açık işleri okur, kaldığınız yerden devam eder. Önemli bir bilgi ortaya çıktığı anda dosyaya yazılır, konuşmanın sonu beklenmez.
4. **Bakım:** Dosyalar şiştikçe Claude onları özetler ve eskiyi arşive alır. Küçük bir Python betiği (`araclar/hafiza_denetimi.py`) yapının sağlığını token harcamadan kontrol eder.

## Kurulum

**Gerekenler:** [Claude Code](https://claude.com/claude-code) (terminal, masaüstü uygulaması veya IDE eklentisi). İsteğe bağlı: Git (değişiklikleri geri alınabilir yapar) ve Python 3 (bakım betiği için).

1. Bilgisayarınızda bir klasör açın, örneğin `Projeler`.
2. Bu depoyu indirin: GitHub'da **Code → Download ZIP**, ardından içindekileri `Projeler` klasörüne çıkarın. Git kullanıyorsanız:
   ```bash
   git clone https://github.com/kamilglhn92/proje-hafiza Projeler
   ```
3. Claude Code'u **bu klasörde** açın ve herhangi bir şey yazın, örneğin "merhaba". Kurulum kendiliğinden başlar.
4. Eski çalışma klasörleriniz varsa `Projeler` içine taşıyın ve Claude'a haber verin; inceleyip departman olarak kaydeder.

> Claude'u her zaman `Projeler` klasöründe (veya bir alt klasöründe) açın. Başka bir yerde açılan oturum bu kuralları görmez.

## İçindekiler

```
Projeler/
├─ CLAUDE.md                  Yönetmelik: roller, iş akışı, hafıza ve token kuralları
├─ AGENTS.md                  Codex uyumluluğu
├─ CATI-HAFIZA/               Ortak hafıza
│  ├─ README.md               Harita: ne nerede, ne zaman okunur
│  ├─ kimlik.md               Siz, kurumunuz, çalışma alanlarınız, kişiler
│  ├─ calisma-ortami.md       Bilgisayar, araçlar, tercihleriniz
│  ├─ departmanlar.md         Departman sicili + personel kadrosu
│  ├─ is-defteri.md           Açık işler (kısa tutulur)
│  ├─ is-defteri-arsiv.md     Kapanan işler
│  ├─ ortak-kararlar.md       Birden fazla departmanı etkileyen kararlar
│  └─ ogrenilenler.md         İşe yarayan / yaramayan yöntemler
├─ _SABLON/                   Yeni departman kalıbı (CLAUDE.md + context/)
├─ .claude/
│  ├─ skills/                 kurulum · yeni-departman · proje-hafizasi
│  └─ agents/                 arastirmaci · denetci
└─ araclar/
   └─ hafiza_denetimi.py      Token harcamadan hafıza denetimi
```

Her departman şu yapıyla doğar:

```
<Departman>/
├─ CLAUDE.md                  Yalnız bu departmana özel kurallar
└─ context/                   Proje özeti, hedefler, kararlar, kurallar, kaynaklar
```

## Temel ilkeler

- **Tek kopya:** Genel kurallar yalnız kökteki `CLAUDE.md` dosyasında durur; departmanlar yalnız kendilerine özel olanı yazar.
- **Katman kuralı:** Tek departmanı ilgilendiren bilgi departmana, birden fazlasını ilgilendiren çatıya yazılır. Aynı bilgi iki yerde tutulmaz.
- **Uydurma yok:** Bilinmeyen "bilgi gerekiyor" diye işaretlenir; tahminle doldurulmaz. Geriye tarih atılmaz.
- **Token ekonomisi:** Her oturumda yalnız kısa dosyalar okunur. Personel (alt ajan) pahalıdır, yalnız gerektiğinde ve tek tek çağrılır.
- **Onay:** Silme, yayımlama, dışarıya mesaj gibi geri alınamaz işler her zaman size sorulur.

## Sık sorulanlar

**Arka planda kendi kendine mi çalışıyor?** Hayır. Sistem bir Claude Code oturumu açıkken yaşar. Her oturum kurallara uyarak yapıyı bir adım büyütür.

**Hangi dilde?** Sistem dosyaları Türkçedir. Claude sizinle kurulumda seçtiğiniz dilde konuşur.

**Codex ile çalışır mı?** `AGENTS.md`, Codex'i aynı kurallara yönlendirir. Beceri ve alt ajan desteği araca göre değişebilir.

**Verilerim nereye gidiyor?** Hafıza dosyaları yalnız sizin bilgisayarınızda durur. Git kullanıyorsanız depo yereldir; uzak sunucuya siz istemedikçe gönderilmez.

## Katkı

Sorun bildirimi ve öneriler için GitHub Issues kullanın. Şablonu kendi kullanımınıza göre değiştirmekte özgürsünüz.

## Lisans

[MIT](LICENSE)

---

## English summary

**Proje Hafızası ("Project Memory")** is a self-assembling workspace template for Claude Code, written in Turkish. Drop it into a folder (e.g. `Projeler`), open Claude Code there, and it runs a short onboarding interview on first launch. From then on it grows by itself as you work.

- **Metaphor:** your folder is an organization, subfolders are departments, Claude acts as the general manager who routes work, keeps memory and spawns helper agents when truly needed.
- **Goal:** no context loss between sessions and minimal token use. Only a few short files are read at the start of each session; durable facts are written the moment they appear; closed tasks are archived; a stdlib-only Python script audits the memory without spending tokens.
- **Contents:** `CLAUDE.md` (the rulebook), `CATI-HAFIZA/` (shared memory), `_SABLON/` (department template), skills (`kurulum` onboarding, `yeni-departman` new department, `proje-hafizasi` memory maintenance), agents (`arastirmaci` researcher, `denetci` reviewer), `araclar/hafiza_denetimi.py`.
- **Install:** download or clone into an empty folder, open Claude Code in that folder and say hello.
- **License:** MIT.
