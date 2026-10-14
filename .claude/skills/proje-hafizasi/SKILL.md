---
name: proje-hafizasi
description: GM bakım zamanı geldiğinde (yaklaşık 10 iş kapandığında veya bir hafıza dosyası şiştiğinde) kendiliğinden; ya da kullanıcı "hafızayı güncelle", "bağlamı denetle", "kaynakları denetle" veya aynı anlama gelen bir ifade kullandığında çatı hafızayı (CATI-HAFIZA) ve departman hafızalarını (<departman>/context) güvenli biçimde güncellemek ya da denetlemek için kullan.
---

# Hafıza Yönetimi (Çatı + Departman)

Üç çalışma biçimi vardır:

1. Hafızayı güncelleme
2. Bağlamı denetleme
3. Kaynakları denetleme

Kullanıcının ifadesine en yakın biçimi seç. Belirsizse hangisinin istendiğini sor.

## Katman kuralı (her biçimde geçerli)

- Bilgi yalnız bir departmanı ilgilendiriyorsa → `<departman>/context/` ilgili dosyası.
- Birden fazla departmanı ilgilendiriyorsa veya kurum geneli bilgiyse (kimlik, kişiler, çalışma ortamı, ortak karar, yöntem dersi) → `CATI-HAFIZA/` ilgili dosyası.
- Departmana yazılmış bir bilgiye ikinci bir departman da ihtiyaç duyarsa bilgi çatıya taşınır ve departmanda yalnız atıf bırakılır. Aynı bilgi iki yerde tutulmaz.
- İş emri izleri yalnız `CATI-HAFIZA/is-defteri.md` dosyasında tutulur.

## Ortak ilkeler

- Önce kökteki `CLAUDE.md`, `CATI-HAFIZA/README.md` ve ilgili departmanın `context/README.md` haritasını oku.
- Yalnız kesinleşmiş, ileride tekrar kullanılacak bilgiyi kalıcı hafızaya işle.
- Geçici fikirleri, reddedilmiş seçenekleri ve doğrulanmamış varsayımları ekleme. Kullanıcının kesinleştirmediği hedef, karar, kural veya sınırı kendiliğinden değiştirme.
- Sohbetin tamamını veya uzun özetini kopyalama.
- Uygun bir dosya varken yeni dosya açma.
- Dosya silmeden önce kullanıcı onayı al. Kullanıcının verdiği bir bilgiyi veya kararı anlamını değiştirecek şekilde yeniden yazma.
- Sonunda yapılan ve önerilen değişiklikleri dosya yollarıyla kısaca bildir.
- Değişiklik bittiğinde git kuruluysa kök depoda kısa bir commit at (push yok). Kendi deposu olan departmanlarda kök depoya commit atılmaz.

## Hafızayı güncelleme

1. Konuşmada kesinleşen hedefleri, kararları, kuralları, sınırları, kişi ve kurum bilgilerini belirle.
2. Her biri için katman kuralına göre hedef dosyayı seç.
3. Hedef dosyadaki mevcut bilgiyle karşılaştır; çelişki varsa sessizce ezme, kullanıcıya bildir.
4. Kesinleşmiş bilgileri işle. Kalıcılığı belirsiz olanları ayrı listele ve sor.
5. "Bilgi gerekiyor" işaretli bir alan doğrulanmış bilgiyle dolduysa işareti kaldır.
6. Dosya oluşturur, taşır, yeniden adlandırır, amacını değiştirir veya silersen ilgili haritayı (`CATI-HAFIZA/README.md` veya `<departman>/context/README.md`) aynı işlemde güncelle.
7. Konuşmada açılan veya kapanan iş varsa `is-defteri.md` dosyasını güncelle.
8. Kullanıcı yeni kaynak eklemediyse `kaynak-indeksi.md` dosyasına dokunma.
9. Hangi bilginin hangi dosyaya işlendiğini bildir.

## Bağlamı denetleme

Kapsam kullanıcı belirtmediyse: çatı hafıza + üzerinde çalışılan departman. "Hepsini denetle" denirse `CATI-HAFIZA/departmanlar.md` dosyasındaki bütün aktif departmanlar.

1. Python varsa önce `python araclar/hafiza_denetimi.py` çalıştır (Windows'ta `py`). Betik harita tutarsızlıklarını, sicilde olmayan klasörleri, şişen dosyaları ve uzayan iş defterini token harcamadan listeler; yalnız onun işaret ettiği dosyaları aç. Python yoksa adımları elle yap.
2. Haritaları ve gösterdikleri dosyaları incele.
3. Haritada olmayan, artık var olmayan, taşınmış veya yeniden adlandırılmış dosyaları belirle.
4. `departmanlar.md` ile gerçek klasörleri karşılaştır: kayıtsız klasör, klasörü olmayan kayıt.
5. Çatı ile departmanlar arasında ve dosyalar arasında çelişkileri, aynı bilginin iki yerde tutulduğu durumları ve eskimiş kayıtları listele.
6. Geçici fikirlerin yanlışlıkla kalıcı hafızaya girip girmediğini kontrol et.
7. `is-defteri.md` dosyasında uzun süredir "açık" veya "kullanıcıdan bekleniyor" durumunda kalan işleri listele.
8. Açık ve risksiz harita yolu düzeltmelerini yap. Anlam değiştirecek düzeltmeleri öner, silme işlemini onaysız yapma.
9. Bulguları `düzeltildi`, `onay bekliyor` ve `bilgi gerekiyor` başlıklarıyla özetle.

## Kaynakları denetleme

1. İlgili departmanın `context/kaynaklar/README.md` ve `kaynak-indeksi.md` dosyalarını oku.
2. `belgeler/`, `veriler/`, `gorseller/`, `ses-ve-video/` klasörlerindeki gerçek dosyaları indeksle karşılaştır. `.gitkeep` kaynak sayılmaz.
3. `baglantilar.md` kayıtlarının indekste karşılığı olup olmadığını kontrol et.
4. İndekste olmayan, yolu değişmiş, silinmiş veya yinelenmiş kaynakları ve eksik alanları (tür, tarih, çıkış noktası, amaç, durum) listele.
5. Orijinal kaynakların içeriğini değiştirme. Doğruluk veya güncelliği tahmin etme; şüpheli durumu bildir.
6. Açık yol ve kayıt hatalarını düzelt; silme veya anlam değişikliği için onay iste.
7. Yapılan değişiklikleri ve kullanıcıdan beklenen kararları özetle.

## Budama (token ekonomisi)

Bağlam denetiminin sonunda:

1. `is-defteri.md` dosyasındaki kapanmış işleri `is-defteri-arsiv.md` dosyasının sonuna taşı.
2. Yaklaşık 150 satırı geçen hafıza dosyasını özetle: güncel ve sık kullanılan bilgi dosyada kalır, ayrıntı ve tarihçe aynı klasörde `<dosya>-arsiv.md` dosyasına taşınır, haritaya işlenir.
3. `ogrenilenler.md` dosyasında birbirini tekrar eden dersleri birleştir.
