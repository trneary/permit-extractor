# invoice-extractor

A Python tool that reads an invoice PDF and extracts important information into a CSV row.

## Why this exists

This exists to obtain important information faster on an invoice PDF, and puts the information into a CSV file. The alternative is opening the PDF in a saved folder, then reading through the whole invoice to aquire this information. 

## How this works

Uses a python script to acess a local PDF file that contains invoice information (invoice number, account number, total due, invoice date, location). It searches each line of the PDF text for a known label, then slices the text after the label to pull the value. It then spits out the information in oragnzed columns in a new CSV File that is saved in the permit_extractor section in the project folder.

## What works

Extracts five fields cleanly from the LAZ Parking invoice: invoice number, account number, total due, invoice date, and location

## What breaks

The scanned PDF with no text layer, the substring matching problem, and the .split()[0] truncating multi-word values. 

## Setup

git clone https://github.com/trneary/permit-extractor.git
cd permit-extractor
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python permit_extractor.py