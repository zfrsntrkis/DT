from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'templates' / '2026.01' / 'Tek Kaynak Formu.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(TTFont('Arial', r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', r'C:\Windows\Fonts\arialbd.ttf'))

PAGE_W, PAGE_H = A4
LEFT = 18*mm
RIGHT = 18*mm
CONTENT_W = PAGE_W - LEFT - RIGHT

styles = getSampleStyleSheet()
styles.add(ParagraphStyle('FormTitle', fontName='Arial-Bold', fontSize=14, leading=17, alignment=TA_CENTER, textColor=colors.black, spaceAfter=3*mm))
styles.add(ParagraphStyle('FormTitleSmall', fontName='Arial-Bold', fontSize=11.5, leading=14, alignment=TA_CENTER, textColor=colors.black, spaceAfter=3*mm))
styles.add(ParagraphStyle('FormSubtitle', fontName='Arial-Bold', fontSize=11, leading=14, alignment=TA_CENTER, textColor=colors.black, spaceAfter=6*mm))
styles.add(ParagraphStyle('Section', fontName='Arial-Bold', fontSize=10.2, leading=13, spaceBefore=3*mm, spaceAfter=2*mm, textColor=colors.black))
styles.add(ParagraphStyle('Body', fontName='Arial', fontSize=9.2, leading=12.5, textColor=colors.black, spaceAfter=2.2*mm))
styles.add(ParagraphStyle('Small', fontName='Arial', fontSize=8.6, leading=11, textColor=colors.black, spaceAfter=1.5*mm))
styles.add(ParagraphStyle('SmallBold', fontName='Arial-Bold', fontSize=8.8, leading=11.5, textColor=colors.black, spaceAfter=1.5*mm))
styles.add(ParagraphStyle('Tiny', fontName='Arial', fontSize=7.8, leading=10, textColor=colors.black))


def P(text, style='Body'):
    return Paragraph(text, styles[style])

def header(canvas, doc):
    canvas.saveState()
    canvas.setFont('Arial', 7.5)
    canvas.setFillColor(colors.HexColor('#555555'))
    canvas.drawRightString(PAGE_W-RIGHT, 10*mm, f'Sayfa {doc.page}')
    canvas.restoreState()

def line_value(label, value, width=CONTENT_W):
    return Table([[P(f'<b>{label}</b>', 'Small'), P(value, 'Small')]], colWidths=[47*mm, width-47*mm], style=TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'), ('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),2),
        ('TOPPADDING',(0,0),(-1,-1),1.2), ('BOTTOMPADDING',(0,0),(-1,-1),1.2),
    ]))

def ruled_box(text, height):
    t=Table([[P(text,'Small')]], colWidths=[CONTENT_W], rowHeights=[height])
    t.setStyle(TableStyle([
        ('BOX',(0,0),(-1,-1),0.7,colors.black), ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),5), ('RIGHTPADDING',(0,0),(-1,-1),5), ('TOPPADDING',(0,0),(-1,-1),5), ('BOTTOMPADDING',(0,0),(-1,-1),5),
    ]))
    return t

def checkbox(text, checked=False, style='Small'):
    mark='☒' if checked else '☐'
    return P(f'{mark} {text}', style)

def section_heading(text):
    return [P(text,'Section'), Table([['']], colWidths=[CONTENT_W], rowHeights=[0.6], style=TableStyle([('LINEBELOW',(0,0),(-1,-1),0.6,colors.black)]))]

story=[]
# Page 1
story += [Spacer(1, 3*mm), P('TEK KAYNAKTAN TEMİN EDİLEN HİZMETLERE İLİŞKİN FORM','FormTitle'), P('Örnek şablon - kişisel ve ticari bilgiler anonimleştirilmiştir','Small')]
story += [Spacer(1, 3*mm), line_value('İDARE:', 'Kurum Adı'), line_value('ALIM YAPAN BİRİM:', 'Şube Müdürlüğü')]
story += section_heading('ALIM YAPILACAK OLAN GERÇEK VEYA TÜZEL TEK KİŞİYE İLİŞKİN BİLGİLER:')
info_data = [
    [P('<b>Adı Soyadı / Ticaret Unvanı, Uyruğu:</b>','Small'), P('Firma1','Small')],
    [P('<b>Açık Tebligat Adresi:</b>','Small'), P('Adres1','Small')],
    [P('<b>Bağlı Olduğu Vergi Dairesi ve Vergi Numarası:</b>','Small'), P('Vergi Dairesi1 / Vergi No1','Small')],
    [P('<b>Telefon ve Faks Numarası:</b>','Small'), P('Telefon1 / Faks1','Small')],
    [P('<b>ÖNGÖRÜLEN TESLİMAT ZAMANI:</b>','Small'), P('Tarih1','Small')],
    [P('<b>YAKLAŞIK BEDEL (TL):</b>','Small'), P('Tutar1 (Yazıyla: Tutar Yazıyla1)','Small')],
]
info=Table(info_data,colWidths=[74*mm, CONTENT_W-74*mm])
info.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#777777')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
story += [info]
story += section_heading('İHTİYAÇ KONUSU HİZMETİN NİTELİKLERİ:')
story += [ruled_box('Kurum Adı Şube Müdürlüğü için Ürün1, Ürün2 ve Ürün3 kalemlerinden oluşan hizmet alımı; 4734 sayılı Kamu İhale Kanununun 22 nci maddesinin (a), (b) veya (c) bendi kapsamında, tek yetkili Firma1 tarafından gerçekleştirilecektir.', 39*mm)]
story += [Spacer(1, 4*mm), P('Bu sayfadaki alanlar uygulamada alım dosyasındaki bilgilerle otomatik doldurulur. Örnek şablonda gerçek kişi, firma, adres ve ürün adları kullanılmamıştır.','Tiny')]
story += [PageBreak()]

# Page 2
story += [P('TEK KAYNAKTAN TEMİN EDİLEN HİZMETLERE İLİŞKİN FORM','FormTitle'), P('Kapsam ve gerekçe','FormSubtitle')]
story += section_heading('GERÇEK VEYA TÜZEL TEK KİŞİDEN ALIMIN HANGİ KAPSAMDA YAPILDIĞI:')
story += [P('(İlgili maddeyi işaretleyiniz.)','Small')]
scope_rows = [
    [P('☐','Small'), P('İhtiyacın sadece gerçek veya tüzel tek kişi tarafından karşılanabileceğinin tespit edilmesi','Small')],
    [P('☐','Small'), P('Sadece gerçek veya tüzel tek kişinin ihtiyaç ile ilgili özel bir hakka sahip olması','Small')],
    [P('☐','Small'), P('Mevcut mal, ekipman ve teknolojiyle uyumun ve standardizasyonun sağlanması için zorunlu olan hizmetin, asıl sözleşmeye dayalı olarak düzenlenecek ve toplam süreleri üç yılı geçmeyecek sözleşmelerle ilk alım yapılan gerçek veya tüzel kişiden temini','Small')],
]
scope=Table(scope_rows,colWidths=[9*mm,CONTENT_W-9*mm], rowHeights=[15*mm,15*mm,29*mm])
scope.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.6,colors.black),('INNERGRID',(0,0),(-1,-1),0.4,colors.HexColor('#777777')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
story += [scope]
story += section_heading('BU ALIMIN GERÇEK VEYA TÜZEL TEK KİŞİDEN YAPILMA SEBEPLERİ:')
story += [ruled_box('Gerekçe1: Ürün1 / hizmet1 için teknik, hukuki veya münhasır hakka dayalı gerekçe burada açıklanacaktır. İlgili belgeler forma eklenecektir. Gerekirse ek sayfa kullanılabilir.', 70*mm)]
story += [Spacer(1, 3*mm), P('(Yukarıda belirtilen hükümlerin uygulanabilir olmasını sağlayan sebepler detaylı olarak yazılacak, bunlara ilişkin belgeler de forma eklenecektir. İstenirse ek bir sayfada devam edilebilir.)','Tiny')]
story += [Spacer(1, 6*mm), P('Dosya ekleri / dayanak belgeleri','Section')]
story += [ruled_box('Ek1 - Yetki veya münhasır hak belgesi<br/>Ek2 - Fiyat/bedel dayanağı<br/>Ek3 - Diğer açıklamalar', 33*mm)]
story += [PageBreak()]

# Page 3
story += [P('TEK KAYNAKTAN TEMİN EDİLEN HİZMETLERE İLİŞKİN FORM','FormTitleSmall'), P('Fiyat araştırması ve uygunluk','FormSubtitle')]
story += section_heading('FİYAT ARAŞTIRMASI')
story += [P('4734 sayılı Kamu İhale Kanununun Doğrudan Temin başlıklı 22 nci maddesinin 2 nci fıkrasına göre bu maddeye göre yapılacak alımlarda ihale yetkilisince görevlendirilecek kişi veya kişiler tarafından piyasada fiyat araştırması yapılarak ihtiyaç temin edilecektir.','Body')]
story += [P('Yaklaşık bedel aşağıda yer alan metotlar kullanılarak gerçekçi bir şekilde tespit edilmiştir (ilgili belgeler eklenecektir):','Body')]
methods = [
    [P('☐','Small'), P('Aynı hizmetin ilgili tek kaynaktan alan diğer kamu/özel tüzel kişiliklerine veya gerçek kişilere sunuluş fiyatı','Small')],
    [P('☐','Small'), P('Aynı hizmet daha önce ilgili tek kaynaktan alındıysa, önceki alım bedelinin ÜFE kullanılarak güncellenmesi; döviz cinsinden ise tespit tarihinde geçerli TCMB döviz alış kuru kullanılması','Small')],
    [P('☐','Small'), P('Firma1 tarafından sunulan güncel fiyat teklifi ve ekli dayanak belgeler','Small')],
]
mt=Table(methods,colWidths=[9*mm,CONTENT_W-9*mm])
mt.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.6,colors.black),('INNERGRID',(0,0),(-1,-1),0.4,colors.HexColor('#777777')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
story += [mt, Spacer(1,5*mm)]
story += [P('Yukarıda belirtilmiş olan sebeplerden dolayı, alım konusu hizmete ilişkin bedelle ilgili piyasada her türlü fiyat araştırması yapılarak 4734 sayılı Kanunun 22 nci maddesinin [(a)/(b)/(c)] bendi kapsamında gerçek veya tüzel tek kişiden alım yapılması uygun görülmüştür.','Body')]
story += [Spacer(1, 8*mm)]
sig=Table([
    [P('<b>Harcama Yetkilisi</b>','SmallBold'), '', ''],
    [P('<b>Adı Soyadı</b> : AdSoyad1','Small'), P('<b>Görevi</b> : Ünvan1','Small'), P('<b>İmza</b> :','Small')],
    [P('<b>Gerçekleştirme Görevlisi</b> : AdSoyad2','Small'), P('<b>Görevi</b> : Ünvan2','Small'), P('<b>İmza</b> :','Small')],
    [P('<b>Fiyat Araştırması Görevlisi</b> : AdSoyad3','Small'), P('<b>Görevi</b> : Ünvan3','Small'), P('<b>İmza</b> :','Small')],
], colWidths=[84*mm,58*mm,CONTENT_W-142*mm])
sig.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.6,colors.black),('INNERGRID',(0,0),(-1,-1),0.4,colors.HexColor('#777777')),('SPAN',(0,0),(-1,0)),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
story += [sig, Spacer(1,5*mm), P('Şablon sürümü: 2026.01 | Örnek alanlar anonimdir.','Tiny')]

doc=SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=RIGHT, leftMargin=LEFT, topMargin=14*mm, bottomMargin=17*mm, title='Tek Kaynaktan Temin Edilen Hizmetlere İlişkin Form', author='DT Project')
doc.build(story, onFirstPage=header, onLaterPages=header)
print(OUT)

