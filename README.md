# invoice-extractor

A Python tool that reads an invoice PDF and extracts important information into a CSV row.

## Why this exists

This exists to obtain important information faster on an invoice PDF, and puts the information into a CSV file. The alternative is opening the PDF in a saved folder, then reading through the whole invoice to aquire this information. 

## How this works

Uses a python script to access a local PDF file that contains invoice information (invoice number, account number, total due, invoice date, location). It searches each line of the PDF text for a known label, then slices the text after the label to pull the value. It then spits out the information in organized columns in a new CSV File that is saved in the permit_extractor section in the project folder.

## What works

Extracts five fields cleanly from the LAZ Parking invoice: invoice number, account number, total due, invoice date, and location

## What breaks

Scanned PDFs have no text layer, so pdfplumber returns empty strings and nothing extracts.

Using `if label in line` matches any line containing the word — searching for "Invoice" would match both "Invoice INV07958830" and "Invoice Date", returning the wrong line. Fixed by switching to `line.startswith(label)`.

`.split()[0]` takes only the first word after the label, so multi-word values like addresses get truncated — location returned "590736" instead of the full address.

## Setup

git clone https://github.com/trneary/permit-extractor.git
cd permit-extractor
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python permit_extractor.py