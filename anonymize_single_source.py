from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial', r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', r'C:\Windows\Fonts\arialbd.ttf'))

out=Path(__file__).resolve().parent/'templates'/'2026.01'/'Tek Kaynak Formu.pdf'
w,h=A4
c=canvas.Canvas(str(out),pagesize=A4)
for page in (1,2):
    c.setFont('Arial-Bold',14); c.drawCentredString(w/2,h-60,'KURUM ADI')
    c.setFont('Arial-Bold',12); c.drawCentredString(w/2,h-90,'TEK KAYNAKTAN TEMİN STANDART FORMU')
    c.setFont('Arial',10)
    c.drawString(55,h-130,'İşin adı: ______________________________________________')
    c.drawString(55,h-155,'Hukuki dayanak: __________  Tarih: ____ / ____ / ______')
    c.drawString(55,h-190,'Tek kaynak gerekçesi: _____________________________________________')
    c.line(55,h-205,w-55,h-205)
    c.drawString(55,h-230,'Ürün1: ____________________   Miktar: _____   Birim fiyat: _____')
    c.drawString(55,h-260,'Ürün2: ____________________   Miktar: _____   Birim fiyat: _____')
    c.drawString(55,h-290,'Ürün3: ____________________   Miktar: _____   Birim fiyat: _____')
    c.drawString(55,h-340,'Firma1: ____________________   Vergi no: ______________')
    c.drawString(55,h-370,'Adres: _________________________________________________________')
    c.drawString(55,150,'AdSoyad1: ____________________   Ünvan1: ____________________')
    c.drawString(55,120,'AdSoyad2: ____________________   Ünvan2: ____________________')
    c.drawString(55,90,'AdSoyad3: ____________________   Ünvan3: ____________________')
    c.showPage()
c.save()
