---
name: kurulum
description: Sistemin ilk kurulumu. CATI-HAFIZA/kimlik.md dosyasında "KURULUM: BEKLIYOR" satırı varsa, kullanıcı ne isterse istesin ilk iş olarak bu beceriyi çalıştır. Ayrıca kullanıcı "kurulumu yeniden yap", "baştan kur", "sistemi tanıt" derse kullan.
---

# İlk Kurulum

Amaç: birkaç kısa soruyla kurumun temelini atmak. Sonrası çalışma sırasında kendiliğinden büyür; burada her şeyi doldurmaya çalışma.

## 1. Selam ve tanıtım (2–3 cümle)

Kullanıcıya kısaca anlat: bu klasör onun "kurumu", alt klasörler "departmanlar", Claude ise "Genel Müdür" olarak hafızayı tutacak ve işleri düzenleyecek. Önce birkaç soru soracağını, toplam 2–3 dakika süreceğini söyle.

## 2. Sorular (tek mesajda, en fazla 6)

1. Sana nasıl hitap edeyim, ne iş yapıyorsun?
2. Bir kurum adına mı çalışıyorsun (şirket, okul, dernek) yoksa kişisel mi? Kurum varsa adı ve ne iş yaptığı.
3. Düzenli olarak hangi tür işler yapıyorsun? (3–5 madde yeterli: ör. teklif hazırlama, raporlama, yazılım, tasarım, ders notları)
4. Bu klasöre taşımak istediğin eski çalışma klasörlerin var mı?
5. Yanıtlarımı nasıl istersin? (dil, kısa/ayrıntılı)
6. Bilgisayarında yönetici (admin) yetkin var mı? Bilmiyorsan "bilmiyorum" de.

Kullanıcı bir soruyu atlarsa üsteleme; o alanı "bilgi gerekiyor" bırak.

## 3. Ortamı kendin yokla (soru sorma)

- İşletim sistemi, `git --version`, `python --version` / `py --version` (Windows'ta PATH'teki `python` bazen Microsoft Store kısayoludur; gerçekten çalışıp çalışmadığına bak).
- Sonuçları `CATI-HAFIZA/calisma-ortami.md` dosyasına yaz.

## 4. Hafızayı doldur

- `CATI-HAFIZA/kimlik.md`: kullanıcı, kurum, çalışma alanları (her biri "departman adayı" olarak; klasör **açma**, ilk gerçek işte açılır).
- `CATI-HAFIZA/calisma-ortami.md`: dil ve yanıt tercihi, admin durumu, araçlar.
- Kullanıcı eski klasörlerini taşıyacağını söylediyse: "Klasörleri bu klasörün içine taşıdığında haber ver, ben inceleyip departman olarak kaydederim" de.

## 5. Git (önerilir)

- Git varsa: kök klasörde `git init`, `.gitignore` zaten var. İlk commit: "Kurulum". Uzak sunucuya gönderme yapma.
- Git yoksa: kullanıcıya git'in değişiklikleri geri alınabilir yaptığını tek cümleyle söyle, kurmayı dayatma. `calisma-ortami.md` dosyasına "git yok" yaz.

## 6. Kapanış

- `CATI-HAFIZA/kimlik.md` içindeki `KURULUM: BEKLIYOR` satırını `KURULUM: TAMAM (YYYY-AA-GG)` yap.
- `is-defteri-arsiv.md` dosyasına "001 · Kurulum · tamamlandı" satırı ekle; `is-defteri.md` dosyasında son numarayı 001 yap.
- Kullanıcıya 3–4 satırla nasıl çalışacağını anlat:
  - "Bana yeni bir iş verdiğinde nereye ait olduğuna ben karar veririm, gerekirse yeni departman açarım."
  - "Önemli bilgiler anında hafızaya yazılır; yeni oturumda kaldığımız yerden devam ederiz."
  - "Claude'u her zaman bu klasörde aç."
- Ardından kullanıcının asıl isteği varsa ona geç.
