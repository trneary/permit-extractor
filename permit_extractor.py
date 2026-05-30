import pdfplumber


def extract_field(text, label):
    lines = text.split("\n")
    for line in lines:
        if label in line:
            parts = line.split(":")
            if len(parts) > 1:
                return parts[1].strip()
    return None

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