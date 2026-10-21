# Değişiklik Günlüğü

## v1.2.1 - 21.10.2026

- Kurumsal PDF örnekleri kaynak yerleşimleri korunarak anonimleştirildi.
- Kişi adları `AdSoyad1` biçimine, görevler `Ünvan1` biçimine dönüştürüldü.
- Ürün ve firma örnekleri `Ürün1` ve `Firma1` biçimine dönüştürüldü.
- Bozuk PDF metin kodlamalarındaki kalan özel ad ve unvan varyantları için eşleştirme düzeltildi.
- Aynı kişi veya unvanın PDF üzerinde üst üste iki kez yazılmasına neden olan yerleşim hatası giderildi.
- Tek Kaynaktan Temin Standart Formu iki sayfalık boş ve anonim yerleşimle güncellendi.
- Dosya Kapağı ve Belge Kontrol Listesi şablon katalogdan kaldırıldı.
- Program ilerlemesi gösterimi arayüzden kaldırıldı.
- `README.md` ve `PROJECT_STATUS.md` ile kurulum, Firebase ve sonraki geliştirme akışı belgelendi.
- GitHub paylaşımı için Firebase ve yönetici ayarları boş şablona ayrıldı; gerçek ayarlar `firebase-config.local.js` içinde tutuluyor.

## v1.2.0 - 21.10.2026

- Firebase yapılandırması varsa Google oturumu kullanılabilir hale getirildi.
- Kullanıcı verileri `users/{uid}/appState/main` altında saklanıyor.
- Girişte bulut verisi yerel taslağa alınıyor.
- Kayıt işlemlerinde Firebase senkronizasyonu deneniyor.
- Bağlantı hatasında yerel taslak korunuyor.
- Tek Kaynaktan Temin formu, 22/a, 22/b ve 22/c için koşullu şablon olarak tanımlandı.
- PDF, Word ve Excel çıktı yardımcıları eklendi.

## v1.0.0 - 21.10.2026

- Kurum, personel ve firma tanımları eklendi.
- Kırtasiye mal alımı örnek verisi eklendi.
- Alım dosyası, kalemler ve firma bazlı teklif tablosu eklendi.
- Firma toplamı ve en uygun teklif hesabı eklendi.
- Belge sırasına göre çıktı oluşturma eklendi.
- JSON dışa aktarma ve geri yükleme eklendi.
- Şablon sürümü `2026.01` olarak tanımlandı.
