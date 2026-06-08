from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

os.makedirs("data/raw", exist_ok=True)

vendors = [
    {"label": "Invoice Number", "total_label": "Total Due"},
    {"label": "Invoice #", "total_label": "Amount Due"},
    {"label": "Invoice No.", "total_label": "Balance Due"},
]

for i in range(1, 31):
    vendor = vendors[i % 3]
    path = f"data/raw/invoice_{i:02d}.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    c.drawString(100, 750, f"{vendor['label']}: INV-{1000+i}")
    c.drawString(100, 730, f"Account: ACC-{2000+i}")
    c.drawString(100, 710, f"Invoice Date: 2026-06-{(i % 28)+1:02d}")
    c.drawString(100, 690, f"Location: {100+i} Main Street, Suite {i}")
    c.drawString(100, 670, f"{vendor['total_label']}: ${i * 150}.00")
    c.save()

print("Generated 30 invoices in data/raw/")