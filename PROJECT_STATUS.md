# Proje Durumu

Son güncelleme: 21.10.2026

## Tamamlananlar

- v1.2.1 uygulama arayüzü ve Firebase yapılandırması depoya alındı.
- Google ile giriş, izinli e-posta listesi ve yönetici kullanıcı ekleme ekranı uygulandı.
- Firestore kayıtları `users/{uid}` altında kullanıcıya özel tutuluyor.
- Kurum bilgileri, personel/unvan, firma, bütçe türü ve bütçe tertibi alanları bulunuyor.
- Alım dosyası kimliği, alım türü, hukuki dayanak, tarih sırası, kalemler, KDV ve firma bazlı birim fiyatlar bulunuyor.
- Firma toplamları ile toplamda en uygun teklif hesaplanıyor.
- 7 kurumsal PDF şablonu ve Tek Kaynaktan Temin Standart Formu `templates/2026.01` altında bulunuyor.
- Örnek PDF kişisel verileri görsel olarak anonimleştirildi: `AdSoyad1`, `Ünvan1`, `Ürün1`, `Firma1` biçimi kullanılıyor.
- Her belge için tarih seçimi ve kronolojik tarih uyarısı bulunuyor.
- Komisyonlarda personel listesinden seçim ve aynı kişinin iki komisyonda tekrar seçilmesini engelleyen kontroller bulunuyor.
- PDF alan eşleştirmeleri, birleşik PDF, Word ve Excel çıktısı için kod mevcut.
- JSON dışa aktarma/geri yükleme, önceki alımı kopyalama ve yerel taslağı koruma akışları bulunuyor.
- Dosya kapağı ve Belge Kontrol Listesi kullanıcı isteğiyle katalogdan kaldırıldı.
- Program ilerleme yüzdesi kullanıcı isteğiyle arayüzden kaldırıldı.

## Bilinen sınırlamalar

- PDF örneklerindeki bazı gömülü metin fontları bozuk kodlandığı için anonimleştirme görsel kaplama ile yapılır; PDF metin katmanında eski metin kalabilir. Son kullanıcı çıktısında görünmemesi sağlanır.
- Tek Kaynaktan Temin formu, taranmış/alan bilgisi okunamayan kaynak PDF yerine boş ve anonim iki sayfalık standart form olarak dağıtılır.
- `firebase-config.js` depoda boş şablondur; gerçek istemci ayarları yerel ve Git dışı `firebase-config.local.js` dosyasındadır. Yönetici anahtarı depoya konulmaz. Firebase Console'da yetkili e-posta ve Google sağlayıcısı ayrıca kontrol edilmelidir.
- Taşınabilir EXE paketleme henüz tamamlanmadı; mevcut sürüm tarayıcıda çalışan yerel web uygulamasıdır.
- Gerçek kurum PDF'lerinin tüm sayfaları için son görsel kabul testi ve gerçek kullanıcı kabul senaryoları sonraki aşamadadır.

## Sıradaki geliştirme sırası

1. PDF şablonlarını tüm sayfalarda görsel olarak kabul testi yapmak ve gerekirse koordinatları düzeltmek.
2. Gerçek bir alım dosyasıyla tarih, komisyon, teklif karşılaştırma ve çıktı akışını uçtan uca test etmek.
3. Firebase Auth/Firestore'u farklı yetkili hesaplarla test etmek; erişim reddi ve çevrimdışı kaydetme senaryolarını doğrulamak.
4. Taşınabilir EXE paketini hazırlamak; uygulama, şablonlar ve ilk çalıştırma ayarlarını tek pakete koymak.
5. v1.3.0 sürüm kaydı, kullanıcı kılavuzu ve dağıtım notlarını eklemek.

## Geliştirme notları

- Şablon değiştirildiğinde önce `templates.json`, sonra `template-fields.json` ve `template-coordinates.json` güncellenir.
- `template_renderer.py` yalnızca çıktı üretiminde kullanılan koordinat katmanıdır; kaynak şablonlar `templates/2026.01` altında tutulur.
- `tmp/` ve Python önbellekleri Git'e gönderilmez.
