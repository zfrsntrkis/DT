from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent / 'templates' / '2026.01'
DOCS = {
 '01-ihtiyac-talep-fisi.pdf':'İHTİYAÇ TALEP FİŞİ',
 '02-yaklasik-maliyet-gorevlendirme.pdf':'YAKLAŞIK MALİYET GÖREVLENDİRME',
 '03-yaklasik-maliyet-tespit-tutanagi.pdf':'YAKLAŞIK MALİYET TESPİT TUTANAĞI',
 '04-dogrudan-temin-onay-belgesi.pdf':'DOĞRUDAN TEMİN ONAY BELGESİ',
 '05-piyasa-fiyat-arastirma-tutanagi.pdf':'PİYASA FİYAT ARAŞTIRMA TUTANAĞI',
 '06-muayene-kabul-gorevlendirme.pdf':'MUAYENE VE KABUL GÖREVLENDİRMESİ',
 '07-muayene-kabul-raporu.pdf':'MUAYENE VE KABUL RAPORU',
 'Tek Kaynak Formu.pdf':'TEK KAYNAKTAN TEMİN STANDART FORMU',
 '08-dosya-kapagi.pdf':'DOĞRUDAN TEMİN DOSYA KAPAĞI',
 '09-belge-kontrol-listesi.pdf':'BELGE KONTROL LİSTESİ',
}
for filename, title in DOCS.items():
    c = canvas.Canvas(str(ROOT / filename), pagesize=A4)
    w, h = A4
    c.setFont('Helvetica-Bold', 14); c.drawCentredString(w/2, h-60, 'KURUM ADI')
    c.setFont('Helvetica-Bold', 12); c.drawCentredString(w/2, h-90, title)
    c.setFont('Helvetica', 10)
    c.drawString(55, h-130, 'İşin adı: ______________________________________________')
    c.drawString(55, h-155, 'Belge tarihi: ____ / ____ / ______    Hukuki dayanak: __________')
    c.line(55, h-180, w-55, h-180)
    c.drawString(55, h-205, 'Kalemler:')
    y = h-235
    for n in range(1, 6):
        c.rect(55, y-5, w-110, 22)
        c.drawString(65, y+3, f'Ürün {n}     Miktar: ______     Birim: ______     Birim fiyat: ______')
        y -= 30
    c.drawString(55, 180, 'Açıklama: __________________________________________________________')
    c.drawString(55, 155, 'İmzacı 1: ____________________     Unvan: ____________________')
    c.drawString(55, 130, 'İmzacı 2: ____________________     Unvan: ____________________')
    c.drawString(55, 105, 'İmzacı 3: ____________________     Unvan: ____________________')
    c.save()
