# Doğrudan Temin Evrak Hazırlama

Sürüm: **v1.2.1**

Bu proje, doğrudan temin dosyasındaki bilgileri bir kez girip kurumsal evrak şablonlarına aktarmak için hazırlanmış kurulum gerektirmeyen web uygulamasıdır. `index.html` dosyası yerel demo modunda açılabilir; Firebase yapılandırması etkin olduğunda Google hesabı ile giriş ve kullanıcıya özel Firestore kayıtları kullanılır.

## Bu depoda neler var?

- `index.html`, `app.js`, `styles.css`: uygulama arayüzü ve iş akışı.
- `firebase-config.js`, `firebase.json`, `firestore.rules`, `firestore.indexes.json`: Firebase bağlantısı ve güvenlik yapılandırması.
- `templates.json`, `template-fields.json`, `template-coordinates.json`: şablon kataloğu ve alan eşleştirmeleri.
- `templates/2026.01/`: 7 kurumsal PDF ile Tek Kaynaktan Temin Standart Formu. Örnek kişi, unvan, ürün ve firma bilgileri anonim yer tutuculara çevrilmiştir (`AdSoyad1`, `Ünvan1`, `Ürün1`, `Firma1`).
- `template_renderer.py`, `export_outputs.py`: PDF alan yerleştirme, birleşik PDF, Word ve Excel çıktısı yardımcıları.
- `anonymize_single_source.py`: boş Tek Kaynak formu üretme aracı. Kaynak örneklerdeki gerçek ad eşleştirmelerini içeren anonimleştirme yardımcısı yerel tutulur ve GitHub'a gönderilmez.
- `PROJECT_STATUS.md`: tamamlanan işler, bilinen sınırlamalar ve sonraki geliştirme sırası.
- `CHANGELOG.md`: sürüm geçmişi.

## Yerelde çalıştırma

1. Klasörü indirin.
2. `index.html` dosyasını doğrudan açın veya klasörde `npx serve .` çalıştırın.
3. Firebase bağlantısı yoksa uygulama demo verisiyle yerel modda çalışır.

## Firebase bağlantısı

1. Firebase Console'da `dogrudantemin-f59f4` projesinde Google Authentication sağlayıcısını etkinleştirin.
2. Firestore Database oluşturun.
3. `firebase-config.js` içindeki Web App ayarlarını kontrol edin. Gerçek ayarları `firebase-config.local.js` dosyasına yazabilirsiniz; bu dosya Git'e alınmaz ve `index.html` tarafından varsa otomatik yüklenir.
4. Firebase CLI ile proje klasöründe `firebase use dogrudantemin-f59f4` ve ardından `firebase deploy --only firestore` çalıştırın.
5. Yönetici hesabı `firestore.rules` içindeki e-posta ile eşleşir. Kullanıcı izinleri uygulamadaki kullanıcı yönetimi ekranından eklenir.

`firebase-config.js` depoda boş şablon olarak bulunur. Gerçek Web API ayarları ve yönetici e-postası yalnızca `firebase-config.local.js` içinde tutulmalıdır. Yönetici/service-account anahtarı bu depoya konulmamalıdır. Firestore erişimi kurallarla oturum açmış kullanıcının kendi `users/{uid}` alanıyla sınırlandırılmıştır.

## Çıktılar

Uygulama PDF, Word ve Excel dosyalarını buluta yüklemez. Kullanıcı istediğinde çıktı üretir ve bilgisayara kaydeder. Çoklu PDF, Word ve Excel üretimi için `export_outputs.py` bir JSON yedeği girdi olarak kullanır.

## Sürümleme

Yeni değişiklikleri `CHANGELOG.md` içine ekleyin, `package.json` sürümünü artırın ve anlamlı bir Git commit'i oluşturun. Şablon düzeni değişirse `templates.json` içindeki şablon sürümünü de güncelleyin.
