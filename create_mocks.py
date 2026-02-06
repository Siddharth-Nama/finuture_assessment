from reportlab.pdfgen import canvas
import os

os.makedirs('documents', exist_ok=True)

def create_hdfc_style(filename):
    c = canvas.Canvas(filename)
    c.drawString(100, 800, "HDFC ERGO General Insurance Company Limited")
    c.drawString(100, 750, "Policy Schedule")
    c.drawString(100, 700, "Policy Number: 12345-67890")
    c.drawString(100, 680, "Name of Policy Holder: Siddharth Nama")
    c.drawString(100, 660, "Premium Amount: Rs. 15,000")
    c.drawString(100, 640, "Sum Assured: Rs. 5,00,000")
    c.drawString(100, 620, "Period of Insurance:")
    c.drawString(100, 600, "Start Date: 01-01-2023")
    c.drawString(100, 580, "End Date: 31-12-2023")
    c.save()

def create_lic_style(filename):
    c = canvas.Canvas(filename)
    c.drawString(100, 800, "Life Insurance Corporation of India")
    c.drawString(100, 750, "Policy Bond")
    c.drawString(100, 720, "Policy No: 987654321")
    c.drawString(100, 700, "Proposer Name: John Doe")
    c.drawString(100, 680, "Installment Premium: INR 50,000")
    c.drawString(100, 660, "Basic Sum Assured: INR 1,00,00,000")
    c.drawString(100, 640, "Date of Commencement: 15/05/2025")
    c.drawString(100, 620, "Date of Maturity: 15/05/2045")
    c.save()

def create_variant_style(filename):
    c = canvas.Canvas(filename)
    c.drawString(50, 800, "MAX LIFE INSURANCE")
    c.drawString(50, 780, "Dear Mr. Valid User,")
    c.drawString(50, 760, "Welcome to Max Life.")
    c.drawString(50, 730, "Your Policy Details are as follows:")
    c.drawString(50, 700, "Policy Number : MAX-2026-XYZ")
    c.drawString(50, 680, "Premium : 25000.00")
    c.drawString(50, 660, "Sum Assured : 2500000")
    c.drawString(50, 640, "Risk Start Date : 10.02.2026")
    c.save()

create_hdfc_style("documents/mock_hdfc.pdf")
create_lic_style("documents/mock_lic.pdf")
create_variant_style("documents/mock_max.pdf")
print("Generated 3 mock PDFs.")
