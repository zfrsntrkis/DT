"""Fill the versioned PDF templates with structured procurement data.

Usage:
  python template_renderer.py data.json output-directory

The source PDFs stay unchanged. Each output is a new PDF with a text overlay.
Coordinates are PDF points measured from the bottom-left corner of an A4 page.
"""
from pathlib import Path
import json, sys
from io import BytesIO

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "templates" / "2026.01"
MAP = {
    "need-request": "01-ihtiyac-talep-fisi.pdf",
    "approximate-cost-assignment": "02-yaklasik-maliyet-gorevlendirme.pdf",
    "approximate-cost-report": "03-yaklasik-maliyet-tespit-tutanagi.pdf",
    "direct-procurement-approval": "04-dogrudan-temin-onay-belgesi.pdf",
    "market-price-research": "05-piyasa-fiyat-arastirma-tutanagi.pdf",
    "inspection-assignment": "06-muayene-kabul-gorevlendirme.pdf",
    "inspection-report": "07-muayene-kabul-raporu.pdf",
    "single-source": "Tek Kaynak Formu.pdf",
}
COORDINATES = json.loads((ROOT / "template-coordinates.json").read_text(encoding="utf-8"))

def text(value):
    return "" if value is None else str(value)

def overlay_page(data, key):
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    c.setFont("Helvetica", 8)
    institution = data.get("institution", {})
    procurement = data.get("procurement", {})
    coords = dict(COORDINATES["common"])
    coords.update(COORDINATES.get("documents", {}).get(key, {}))
    c.drawString(*coords["institution"], text(institution.get("name")))
    c.drawString(*coords["workName"], text(procurement.get("workName")))
    dates = procurement.get("documentDates", {})
    c.drawString(*coords["date"], text(dates.get("0", procurement.get("date"))))
    c.drawString(*coords["law"], text(procurement.get("law")))
    items = procurement.get("items", [])
    y = coords["itemsStart"][1]
    for index, item in enumerate(items[:14], 1):
        c.drawString(58, y, text(index))
        c.drawString(95, y, text(item.get("description"))[: sixty_chars])
        c.drawRightString(470, y, text(item.get("quantity")))
        c.drawString(485, y, text(item.get("unit")))
        y -= coords["itemsRowHeight"]
    personnel = data.get("personnel", [])
    committees = procurement.get("committees", {})
    cost = [personnel[i] for i in committees.get("cost", []) if i < len(personnel)]
    inspection = [personnel[i] for i in committees.get("inspection", []) if i < len(personnel)]
    c.drawString(*coords["committeeCost"], "Yaklaşık maliyet komisyonu: " + ", ".join(text(x.get("name")) for x in cost))
    c.drawString(*coords["committeeInspection"], "Muayene ve kabul komisyonu: " + ", ".join(text(x.get("name")) for x in inspection))
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]

sixty_chars = 64

def render(data, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    for key, filename in MAP.items():
        source = TEMPLATE_DIR / filename
        if not source.exists():
            continue
        original = PdfReader(str(source))
        writer = PdfWriter()
        for number, page in enumerate(original.pages):
            if number == 0:
                page.merge_page(overlay_page(data, key))
            writer.add_page(page)
        writer.write(str(output_dir / f"{key}-doldurulmus.pdf"))

def from_app_state(state, output_dir):
    """Render the last procurement from an app backup JSON."""
    procurement = (state.get("procurements") or [{}])[-1]
    render({
        "institution": state.get("institution", {}),
        "personnel": state.get("personnel", []),
        "companies": state.get("companies", []),
        "procurement": procurement,
    }, output_dir)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Kullanım: python template_renderer.py data.json çıktı-klasörü")
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if "procurements" in payload:
        from_app_state(payload, Path(sys.argv[2]))
    else:
        render(payload, Path(sys.argv[2]))
