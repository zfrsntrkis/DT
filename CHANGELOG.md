# Değişiklik Günlüğü

## v1.0.0 - 21.10.2026

- Kurum, personel ve firma tanımları eklendi.
- Kırtasiye mal alımı örnek verisi eklendi.
- Alım dosyası ve benzersiz dosya kimliği eklendi.
- Ürün/hizmet kalemleri ve firma bazlı birim fiyat tablosu eklendi.
- Firma toplamı ve en uygun teklif hesabı eklendi.
- Dosya kapağı ve belge kontrol listesi önizlemesi eklendi.
- Belge sırasına göre çıktı oluşturma eklendi.
- 22/a, 22/b ve 22/c için Tek Kaynaktan Temin koşulu eklendi.
- Program ve dosya ilerleme yüzdesi eklendi.
- Önceki alımdan yeni dosya oluşturma eklendi.
- JSON dışa aktarma ve geri yükleme eklendi.
- Şablon sürümü `2026.01` olarak tanımlandı.
- Firebase Authentication ve Firestore güvenlik altyapısı eklendi.

## Sonraki sürümler

- `v1.1.0`: Gerçek kurum PDF/DOCX şablon alan eşleştirmeleri.
- `v1.2.0`: Firebase proje bağlantısı ve çevrimdışı senkronizasyon.
- `v1.3.0`: Taşınabilir EXE paketleme.

## v1.2.0 - 21.10.2026

- Firebase yapılandırması varsa Google oturumu kullanılabilir hale getirildi.
- Kullanıcı verileri `users/{uid}/appState/main` altında saklanıyor.
- Girişte bulut verisi yerel taslağa alınıyor.
- Kayıt işlemlerinde Firebase senkronizasyonu deneniyor.
- Bağlantı hatasında yerel taslak korunuyor.
- `templates/2026.01/Tek Kaynak Formu.pdf` örnek şablonu eklendi.
- Tek Kaynak Formu, 22/a, 22/b ve 22/c için koşullu şablon olarak tanımlandı.

