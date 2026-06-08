from pathlib import Path
from permit_extractor import extract_invoice

PDF_DIR = Path("data/raw")
results = []

for pdf_path in PDF_DIR.glob("*.pdf"):
    result = extract_invoice(str(pdf_path))
    if result:
        results.append(result)
    else:
        print(f"FAILED: {pdf_path.name}")

print(f"Extracted {len(results)} of {len(list(PDF_DIR.glob('*.pdf')))} invoices")