import pdfplumber
import re

class ParserService:
    def parse(self, file_path):
        text = self._extract_text(file_path)
        with open('debug_log.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n--- DEBUG TEXT START for {file_path} ---\n{text}\n--- DEBUG TEXT END ---\n")
        
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
        pattern = r"Policy\s*(?:No\.?|Number)?\s*[:\-\s]*([A-Za-z0-9\-\/]+)"
        match = re.search(pattern, text, re.IGNORECASE)
        with open('debug_log.txt', 'a', encoding='utf-8') as f:
            f.write(f"Policy Pattern: {pattern}\nMatch: {match.group(1) if match else 'NONE'}\n")
        return match.group(1) if match else None

    def _extract_holder_name(self, text):
        pattern = r"(?:Name|Holder|Proposer)\s*(?:of\s*Policy\s*Holder|Name)?\s*[:\-\s]*([A-Za-z\s\.]+)"
        match = re.search(pattern, text, re.IGNORECASE)
        result = match.group(1).strip() if match else None
        with open('debug_log.txt', 'a', encoding='utf-8') as f:
            f.write(f"Holder Pattern: {pattern}\nMatch: {result}\n")
        return result

    def _extract_premium_amount(self, text):
        pattern = r"(?:Premium|Installment\s*Premium)\s*(?:Amount)?\s*[:\-\s]*(?:Rs\.?|INR)?\s*([\d,]+\.?\d{0,2})"
        match = re.search(pattern, text, re.IGNORECASE)
        with open('debug_log.txt', 'a', encoding='utf-8') as f:
            f.write(f"Premium Pattern: {pattern}\nMatch: {match.group(1) if match else 'NONE'}\n")
        return match.group(1) if match else None

    def _extract_sum_assured(self, text):
        pattern = r"(?:Basic\s*)?Sum\s*Assured\s*[:\-\s]*(?:Rs\.?|INR)?\s*([\d,]+\.?\d{0,2})"
        match = re.search(pattern, text, re.IGNORECASE)
        with open('debug_log.txt', 'a', encoding='utf-8') as f:
            f.write(f"Sum Assured Pattern: {pattern}\nMatch: {match.group(1) if match else 'NONE'}\n")
        return match.group(1) if match else None

    def _extract_date(self, text, keyword):
        pattern = rf"{keyword}\s*(?:Date)?\s*(?:of)?\s*[:\-\s]*(\d{{1,2}}[-/.]\d{{1,2}}[-/.]\d{{2,4}})"
        match = re.search(pattern, text, re.IGNORECASE)
        
        with open('debug_log.txt', 'a', encoding='utf-8') as f:
            f.write(f"Date Pattern ({keyword}): {pattern}\nMatch: {match.group(1) if match else 'NONE'}\n")
        
        return match.group(1) if match else None

