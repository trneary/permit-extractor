import pdfplumber
import csv

def extract_field(text, label):
    lines = text.split("\n")
    for line in lines:
        if line.startswith(label):
            value = line[len(label):]
            value = value.lstrip(": ").strip()
            # take only the first token (everything before the first whitespace)
            value = value.split()[0]
            return value
    return None

def main():
    PDF_PATH = "C:/Users/neary/Downloads/invoice.pdf"

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

    print(invoice_data)

    with open("invoice.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=invoice_data.keys())
        writer.writeheader()
        writer.writerow(invoice_data)

if __name__ == "__main__":
    main()