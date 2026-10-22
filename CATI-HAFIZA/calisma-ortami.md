# Çalışma Ortamı

Bu dosya, bütün departmanlarda geçerli olan bilgisayar, araç ve çalışma tercihlerini tutar. Kurulumda doldurulur; araç yolları doğrulandıkça eklenir.

## Bilgisayar

- Çalışma biçimi: Claude Code bulut oturumları (claude.ai/code); kod GitHub repolarında durur. Kullanıcının kendi bilgisayarı: bilgi gerekiyor.
- Yönetici (admin) yetkisi: bilgi gerekiyor (bulut oturumunda gerekmiyor).
- Bulut klasörü: Google Drive (bağlı; kaynak dosyalar buradan alınabilir).

## Araçlar

| Araç | Yol / komut | Durum |
|---|---|---|
| Git | `git` | bulut oturumunda var (2026-10-15) |
| Python 3 | `python3` | bulut oturumunda var (2026-10-15) |
| Node.js / npm | `node`, `npm` | bulut oturumunda var (Node 22, 2026-10-15) |

## Beceri ve bağlantı kullanımı

- GM, işe uyan beceriyi (skill) ve bağlantıyı (MCP) kendisi çağırır; kullanıcının `/ad` yazması gerekmez.
- Bağlantı ile dışarıya bir şey gönderme, yayımlama veya silme kullanıcı onayı olmadan yapılmaz.

| İş | Beceri / bağlantı |
|---|---|
| Hafıza bakımı | `proje-hafizasi` |
| Yeni iş alanı | `yeni-departman` |
| Drive'dan dosya alma | Google Drive bağlantısı |
| GitHub (repo okuma/yazma, PR) | GitHub bağlantısı; yalnız oturuma eklenmiş repolar |

## Kullanıcının çalışma tercihleri

- Dil: Türkçe
- Yanıt uzunluğu: kısa, sonuç önce, tek net öneri. Filtresiz; yanlışsa doğrudan söyle (kullanıcı tercihi)
- Erişim: GM'nin bütün hesaplarına (Google dahil) geniş erişimi olsun; kişisel asistan gibi çalışılsın, erişim engeli istemiyor (kullanıcı beyanı, 2026-10-22). Kimlik bilgisi yine dosyaya/sohbete yazılmaz; bağlantılar ve ortam gizli değerleriyle verilir

## Bilinen tuzaklar

<!-- Bu bilgisayarda karşılaşılan teknik tuzaklar; ör. özel karakterli klasör adlarında tırnak gerekmesi. -->

- Bulut oturumu yeni GitHub reposu oluşturamıyor (403). Yeni repoyu kullanıcı github.com/new'den açar, sonra oturuma eklenir.
- Bulut oturumunun Google Cloud'a (Console, API anahtarı) erişimi yok. Kullanıcının bilgisayarındaki Chrome eklentisine kurallı bir talimat yazılır (ödeme yok, silme yok, anahtar sohbete yazılmaz, beklenmedik ekranda durup sorar); eklenti işi yapar, raporu buraya gelir.
- Supabase bağlantısında Edge Function silme aracı yok; `execute_sql` ile `delete` onay kapısı oturuma ulaşmadığı için zaman aşımına uğruyor. Silmeyi kullanıcı panelden ya da SQL Editor'dan yapar, sonra buradan sayılarak doğrulanır.
