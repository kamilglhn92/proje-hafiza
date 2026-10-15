# İş Defteri

Bu dosya kullanıcının getirdiği işleri kaydeder. Birkaç dakikalık soru-cevaplar yazılmaz. Ayrıntı işin yapıldığı departmanın hafızasına yazılır; burada yalnız iz kalır.

Durum değerleri: `açık` · `kullanıcıdan bekleniyor` · `bekliyor (dış)` · `tamamlandı` · `iptal`

- Yeni iş numarası almadan hemen önce bu dosyayı yeniden oku; aynı anda çalışan iki oturum aynı numarayı alabilir.
- Kapanan iş bu dosyadan silinir ve `is-defteri-arsiv.md` dosyasının sonuna eklenir. Bu dosya her oturumda okunduğu için kısa kalmalıdır.
- Yarıda kalan işin satırına `DEVAM:` ile nerede kalındığı ve sıradaki adım yazılır.

## Açık işler

| No | Tarih | İş | Departman | Durum | Bekleyen |
|---|---|---|---|---|---|
| 002 | 2026-10-15 | Kütüphane uygulaması: ayrı repo + Faz 1 | `kutuphanem` | kullanıcıdan bekleniyor | Kullanıcı boş `kutuphanem` reposunu açacak. DEVAM: kod hazır, ilk commit yerelde; repo açılınca oturuma ekle ve gönder. Uygulamanın kendi açık işleri o reponun `hafiza/is-defteri.md` dosyasında. |

Son verilen iş no: **002**.
