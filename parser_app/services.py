import pdfplumber
import re

class ParserService:
    def parse(self, file_path):
        text = self._extract_text(file_path)
        print(f"--- DEBUG TEXT START for {file_path} ---\n{text}\n--- DEBUG TEXT END ---")
        data = {
            'policy_number': self._extract_policy_number(text),
            'holder_name': self._extract_holder_name(text),
            'premium_amount': self._extract_premium_amount(text),
            'sum_assured': self._extract_sum_assured(text),
            'coverage_start_date': self._extract_date(text, r'(?:Start\s*Date|Commencement|Risk\s*Start\s*Date)'),
            'coverage_end_date': self._extract_date(text, r'(?:End\s*Date|Maturity)'),
            'raw_data': {'full_text': text}
        }
        return data

    def _extract_text(self, file_path):
        text = ""
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
        except Exception as e:
            print(f"Error reading PDF: {e}")
        return text

    def _extract_policy_number(self, text):
        # Matches: Policy No: 123, Policy Number : 123, Policy No 123
        pattern = r"Policy\s*(?:No\.?|Number)?\s*[:\-\s]*([A-Za-z0-9\-\/]+)"
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1) if match else None

    def _extract_holder_name(self, text):
        # Matches: Name: John, Name of Policy Holder: John, Proposer Name: John
        pattern = r"(?:Name|Holder|Proposer)\s*(?:of\s*Policy\s*Holder|Name)?\s*[:\-\s]*([A-Za-z\s\.]+)"
        match = re.search(pattern, text, re.IGNORECASE)
        # Clean up result (remove trailing newlines/spaces)
        return match.group(1).strip() if match else None

    def _extract_premium_amount(self, text):
        # Matches: Premium: 1000, Premium Amount: 1000, Installment Premium: 1000
        pattern = r"(?:Premium|Installment\s*Premium)\s*(?:Amount)?\s*[:\-\s]*(?:Rs\.?|INR)?\s*([\d,]+\.?\d{0,2})"
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1) if match else None

    def _extract_sum_assured(self, text):
        # Matches: Sum Assured: 1000, Basic Sum Assured: 1000
        pattern = r"(?:Basic\s*)?Sum\s*Assured\s*[:\-\s]*(?:Rs\.?|INR)?\s*([\d,]+\.?\d{0,2})"
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1) if match else None

    def _extract_date(self, text, keyword):
        # Matches: Start Date: 01-01-2000, Date of Commencement: 01/01/2000
        # Keyword is a regex partial, e.g., (?:Start Date|Commencement)
        pattern = rf"{keyword}\s*(?:Date)?\s*(?:of)?\s*[:\-\s]*(\d{{1,2}}[-/.]\d{{1,2}}[-/.]\d{{2,4}})"
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1) if match else None

