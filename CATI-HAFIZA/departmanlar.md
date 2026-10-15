# Departman Sicili

Bu dosya kurumun bütün departmanlarını (alt klasörleri) kaydeder. GM bir işi yönlendirirken bu tabloya bakar. Yeni departman `yeni-departman` becerisiyle açılır ve aynı işlemde buraya eklenir. Klasör adı değişirse tablo aynı işlemde güncellenir.

| Departman (klasör) | Görev alanı | Tür | Durum | Hafıza | Sık kullanılan personel |
|---|---|---|---|---|---|
| `CATI-HAFIZA/` | Kurumun ortak hafızası | Yönetim | Aktif | Bu klasörün kendisi | — |
| `_SABLON/` | Yeni departman şablonu. Doğrudan iş yapılmaz | Şablon | — | — | — |
| `kutuphanem` (ayrı repo: `kamilglhn92/kutuphanem`, gizli) | Kişisel kütüphane ve okuma takibi uygulaması (PWA) | Yazılım projesi | Aktif | Kendi reposunda (CLAUDE.md + hafiza klasörü). Burada kopya tutulmaz | — |

## Personel kadrosu

| Personel | Görev | Yazma yetkisi |
|---|---|---|
| `arastirmaci` | Web ve belge araştırması, kaynaklı rapor | Yok (salt okur) |
| `denetci` | Teslim öncesi bağımsız kontrol | Yok (salt okur) |

Yeni personel tanımlandıkça bu tabloya eklenir. Tanımlar `.claude/agents/` klasöründedir.

## Yönlendirme ipuçları

<!-- Departmanlar oluştukça "şu tür iş → şu departman" kuralları buraya eklenir. -->

- Kütüphane, okuma takibi, okuma raporları → `kutuphanem` reposu. O repoda çalışılır; bu repoda yalnız sicil satırı ve iş defteri izi kalır.
