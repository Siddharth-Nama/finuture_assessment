import requests
import os
import glob

def verify_extraction():
    files = glob.glob("documents/mock_*.pdf")
    if not files:
        print("No PDF files found in documents/")
        return

    print(f"Found {len(files)} files to verify.")
    
    url = "http://127.0.0.1:8000/api/upload/"
    
    for file_path in files:
        print(f"\nProcessing {file_path}...")
        try:
            with open(file_path, 'rb') as f:
                response = requests.post(url, files={'file': f})
                
            if response.status_code == 201:
                data = response.json()
                print("SUCCESS")
                extracted = data.get('extracted_data', [{}])[0]
                print(f"Policy No: {extracted.get('policy_number')}")
                print(f"Premium: {extracted.get('premium_amount')}")
                print(f"Sum Assured: {extracted.get('sum_assured')}")
            else:
                print(f"FAILED: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    verify_extraction()
