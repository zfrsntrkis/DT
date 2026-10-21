# Doğrudan Temin Evrak Hazırlama v1.2.0

Kurulumsuz çalışacak taşınabilir uygulamanın ilk kararlı sürümüdür. `index.html` tarayıcıda açılarak demo modunda kullanılabilir. Firebase bağlantısı için `firebase-config.js` içindeki ayarlar doldurulur.

## v1.2.0 kapsamı

- Google ile giriş ve kullanıcıya özel Firestore kayıtları
- Kurum, personel, firma, bütçe türü ve bütçe kalemi tanımları
- Alım dosyası, kalem ve firma teklif tablosu
- Kalem/toplam değerlendirme, KDV ve toplam hesaplama
- Belge tarih sırası ve eksik veri kontrolleri
- JSON dışa aktarma/geri yükleme
- Şablon sürümü ve program sürümü kaydı
- Firebase'de kurum, personel, firma, alım, kalem ve teklif alt kayıtlarının kullanıcı bazlı saklanması
- Tek Kaynaktan Temin örnek şablonunun `templates/2026.01` altında dağıtılması
- Dosya kapağı, belge kontrol listesi, evrak önizleme ve yerel çıktı hazırlama

Firebase kuralları `firestore.rules` dosyasındadır. Uygulama buluta PDF, Word veya Excel yüklemez; çıktılar kullanıcı istediğinde bilgisayarda hazırlanır.

## Firebase v1.2 kurulumu

1. Firebase Console'da Authentication > Google sağlayıcısını etkinleştirin.
2. Firestore Database oluşturun ve `firestore.rules` kurallarını dağıtın.
3. `firebase-config.js` içine Web App yapılandırmasını girin.
4. Geliştirme sırasında `firebase deploy --only firestore` komutunu çalıştırın.

Firebase bilgileri girilmeden uygulama güvenli yerel demo modunda çalışır.

