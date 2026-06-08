from pathlib import Path
from permit_extractor import extract_invoice
import csv

PDF_DIR = Path("data/raw")
results = []
failures = []

for pdf_path in PDF_DIR.glob("*.pdf"):
    try:
        result = extract_invoice(str(pdf_path))
        if result:
            result["source_file"] = pdf_path.name
            results.append(result)
        else:
            failures.append({"file": pdf_path.name, "reason": "returned None"})
    except Exception as e:
        failures.append({"file": pdf_path.name, "reason": str(e)})

# Write CSV
all_fields = set()
for r in results:
    all_fields.update(r.keys())
all_fields.discard("source_file")
fieldnames = ["source_file"] + sorted(all_fields)

with open("invoices_batch.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    for row in results:
        writer.writerow(row)

# Write failures log
with open("failures.log", "w") as f:
    for fail in failures:
        f.write(f"{fail['file']}: {fail['reason']}\n")

print(f"Extracted {len(results)} of {len(list(PDF_DIR.glob('*.pdf')))} invoices")
print(f"Failures logged: {len(failures)}")