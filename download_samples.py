import requests
import os

urls = [
    ("documents/hdfc_sample.pdf", "https://www.hdfcergo.com/images/default-source/documents/health-insurance/optima-restore/policy-wordings/optima-restore-policy-wordings.pdf"),
    ("documents/tata_sample.pdf", "https://www.tataaia.com/content/dam/tataaia/life-insurance/pdf/sample-policy-document/Fortune-Guarantee-Plus-Sample-Policy-Document.pdf"),
    ("documents/max_sample.pdf", "https://www.maxlifeinsurance.com/content/dam/corporate/brochures/MaxLife-SmartWealthPlan-PolicyDocument.pdf")
]

os.makedirs('documents', exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

for filename, url in urls:
    try:
        print(f"Downloading {url}...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
