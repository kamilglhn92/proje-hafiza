---
name: yeni-departman
description: Yeni bir proje veya sürekli iş alanı geldiğinde ve mevcut departmanların hiçbirine uymadığında yeni departman (alt klasör) açmak için kullan. Ayrıca hafızası boş olan mevcut bir departmanı kurmak (kuruluş görüşmesi) için kullan. Tetikleyiciler: "yeni proje", "yeni iş geldi", "departman aç", "bunu ayrı tutalım", "kuruluş görüşmesi", "departmanı kur".
---

# Yeni Departman Açma / Departman Kurma

Bu beceri, GM'nin yeni bir departmanı şablondan açmasını veya hafızası boş bir departmanı kurmasını sağlar. Amaç: departman hafızası ilk günden doğru ve az ama yeterli olsun.

## Önce karar: departman mı, değil mi?

Departman aç:
- İş birden fazla oturum sürecekse, kendi dosyaları ve çıktıları olacaksa veya tekrar edecekse.

Departman açma:
- Tek seferlik, birkaç dosyalık küçük işse. İş GM düzeyinde yapılır ve `is-defteri.md` dosyasına yazılır.
- İş mevcut bir departmanın alanına giriyorsa (bkz. `CATI-HAFIZA/departmanlar.md`). O departmanda çalışılır.

Emin değilsen kullanıcıya tek cümleyle sor.

## A) Yeni departman açma

1. **Kısa görüşme**: Yalnız kullanıcının bilebileceği ve konuşmadan/dosyalardan çıkmayan gerçekleri sor; en fazla 3 soru, tek mesajda. Cevabı zaten verilmiş olanı sorma. Aday sorular:
   - Bitmiş hâli neye benzeyecek (belge, etiket, program, sunum…)?
   - Kim istedi, kim onaylayacak, son tarih var mı?
   - Elinde kaynak var mı (dosya, örnek, eski çalışma)?
   Cevap gelmeden de başlanabiliyorsa başla; eksikleri "bilgi gerekiyor" diye işaretle.
2. **Klasör adı**: GM belirler. Kısa ve anlaşılır olmalı; aynı adlı klasör olmamalı. Boşluk ve Türkçe karakter kullanılabilir ama komut satırında tırnak gerektirir; mümkünse sade ad seç. Kullanıcıya bildirilir, onay beklenmez.
3. **Klasörü aç**: `_SABLON/` klasörünü yeni adla kopyala. `_SABLON` klasörünün kendisini değiştirme.
4. **CLAUDE.md**: `{{DEPARTMAN_ADI}}` yerine departman adını yaz. "Departmana özel kalıcı talimatlar" bölümüne yalnız görüşmede kesinleşen ve her görevde geçerli olan kısa kuralları yaz.
5. **Hafıza**: Görüşme cevaplarını ilgili dosyalara işle:
   - `context/proje-ozeti.md`: ad, tanım, amaç, kapsam, mevcut durum.
   - `context/hedefler.md`: çıktı ve son tarih.
   - `context/kurallar-ve-sinirlar.md`: kurallar ve yasaklar.
   - Bilinmeyen alanları boş bırak; tahmin yazma.
6. **Kaynaklar**: Kullanıcı kaynak verdiyse uygun `context/kaynaklar/` alt klasörüne koy ve `kaynak-indeksi.md` dosyasına kaydet. Orijinali değiştirme.
7. **Çatıya kayıt**:
   - `CATI-HAFIZA/departmanlar.md` tablosuna satır ekle (klasör, görev alanı, tür, durum, hafıza, olası personel).
   - `CATI-HAFIZA/is-defteri.md` dosyasına iş kaydı aç.
   - Görüşmede yeni kişi veya kurum bilgisi çıktıysa katman kuralına göre çatıya işle.
8. **Commit**: Git kuruluysa kök depoda `Yeni departman: <ad>` mesajıyla commit at (push yok).
9. **Rapor**: Açılan klasörü, doldurulan dosyaları, boş kalan alanları ve "kullanıcıdan beklenenler"i bildir. Ardından asıl işe geç.

## B) Taşınan veya hafızası boş bir klasörü departmana dönüştürme

Kullanıcı eski bir çalışma klasörünü kurumun içine taşıdığında veya sicilde olmayan bir klasör fark edildiğinde uygulanır.

1. Klasördeki mevcut dosyaları incele: çıktılar, görseller, belgeler, son değişiklik tarihleri. Neyin ne olduğunu dosyalardan çıkar. Klasörün adına bakarak hüküm verme.
   - Klasörün **kendi hafıza düzeni** varsa (ör. kendi notları, devir belgesi, karar defteri), o düzeni koru. Yalnız klasöre, okunacak dosyaları sırayla gösteren kısa bir `CLAUDE.md` ekle ve sicile işle; `context/` yapısını dayatma.
   - Klasörün **kendi git deposu** varsa kök deponun `.gitignore` dosyasına ekle.
2. Çıkardığını kullanıcıya kısa bir özetle doğrulat. A-1'deki sorulardan yalnız cevabı dosyalardan çıkmayanları sor.
3. A-5, A-6 ve A-7 adımlarını uygula. Klasördeki mevcut dosyaları taşıma veya yeniden adlandırma; gerekiyorsa öner ve onay al.
4. `is-defteri.md` dosyasındaki ilgili kuruluş işini `tamamlandı` yap, `departmanlar.md` dosyasında "Hafıza" sütununu güncelle.
5. Commit ve rapor (A-8, A-9).
