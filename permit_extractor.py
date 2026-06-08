import pdfplumber
import csv

def extract_field(text, label):
    """Search text line by line for a label, return the value that follows it."""
    lines = text.split("\n")
    for line in lines:
        if line.startswith(label):
            value = line[len(label):]
            value = value.lstrip(": ").strip()
            return value
    print(f"Warning: could not find {label}")
    return ""

def extract_field_any(text, *labels):
    """Try multiple label variants, return the first match."""
    for label in labels:
        value = extract_field(text, label)
        if value:
            return value
    return ""

def extract_invoice(pdf_path: str) -> dict:
    """Opens a PDF, extracts structured fields, returns them as a dict."""
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text
    if not full_text.strip():
        return None
    return {
        "invoice_number": extract_field_any(full_text, "Invoice Number", "Invoice #", "Invoice No.", "Invoice"),
        "account_number": extract_field_any(full_text, "Account Number", "Account No.", "Account"),
        "total_due": extract_field_any(full_text, "Total Due", "Amount Due", "Balance Due", "Total"),
        "invoice_date": extract_field_any(full_text, "Invoice Date", "Date"),
        "location": extract_field_any(full_text, "Location", "Address", "Bill To"),
    }
def main():
    """Read a PDF invoice, extract structured fields, and write them to a CSV.""" 
    PDF_PATH = "data/raw/invoice.pdf"

    with pdfplumber.open(PDF_PATH) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text()

    invoice_data = {
        'invoice_number': extract_field(full_text, 'Invoice'),
        'account_number': extract_field(full_text, 'Account'),
        'total_due': extract_field(full_text, 'Total Due'),
        'invoice_date': extract_field(full_text, 'Invoice Date'),
        'location': extract_field(full_text, 'Location'),
    }

    with open("invoice.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=invoice_data.keys())
        writer.writeheader()
        writer.writerow(invoice_data)

if __name__ == "__main__":
    main()