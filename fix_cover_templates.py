from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

root=Path(__file__).resolve().parent/'templates'/'2026.01'
w,h=A4
docs=['İhtiyaç Talep Fişi','Yaklaşık Maliyet Görevlendirme','Yaklaşık Maliyet Tespit Tutanağı','Doğrudan Temin Onay Belgesi','Piyasa Fiyat Araştırma Tutanağı','Muayene ve Kabul Görevlendirmesi','Muayene ve Kabul Raporu']

c=canvas.Canvas(str(root/'08-dosya-kapagi.pdf'),pagesize=A4)
c.setFont('Helvetica-Bold',16); c.drawCentredString(w/2,h-70,'KURUM ADI')
c.setFont('Helvetica-Bold',14); c.drawCentredString(w/2,h-105,'DOĞRUDAN TEMİN DOSYA KAPAĞI')
c.setFont('Helvetica',11)
for y,label in [(h-165,'İşin adı:'),(h-200,'Alım türü:'),(h-235,'Hukuki dayanak:'),(h-270,'Belge tarihi:'),(h-305,'Bütçe türü:'),(h-340,'Bütçe tertibi:'),(h-375,'Yaklaşık maliyet:')]:
    c.drawString(70,y,label); c.line(190,y-2,w-70,y-2)
c.setFont('Helvetica-Bold',12); c.drawString(70,h-435,'DOSYADA BULUNAN BELGELER')
c.setFont('Helvetica',10)
for i,d in enumerate(docs):
    c.rect(75,h-475-i*30,14,14); c.drawString(100,h-474-i*30,d)
c.save()

c=canvas.Canvas(str(root/'09-belge-kontrol-listesi.pdf'),pagesize=A4)
c.setFont('Helvetica-Bold',16); c.drawCentredString(w/2,h-70,'BELGE KONTROL LİSTESİ')
c.setFont('Helvetica',10); c.drawString(70,h-110,'İşin adı: _________________________________________________')
for i,d in enumerate(docs):
    y=h-160-i*38; c.rect(70,y,14,14); c.drawString(100,y+2,d); c.drawString(400,y+2,'Tarih: __________')
c.drawString(70,100,'Kontrol eden: ____________________    İmza: ______________')
c.save()
