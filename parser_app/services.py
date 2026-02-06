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
        # Matches: Policy No: 123, Policy Number : 123, Policy No 123
        # Must contain at least one digit to avoid matching headers like "Policy Schedule"
        pattern = r"Policy\s*(?:No\.?|Number)?\s*[:\-\s]*([A-Za-z0-9\-\/]*\d+[A-Za-z0-9\-\/]*)"
        match = re.search(pattern, text, re.IGNORECASE)
        with open('debug_log.txt', 'a', encoding='utf-8') as f:
            f.write(f"Policy Pattern: {pattern}\nMatch: {match.group(1) if match else 'NONE'}\n")
        return match.group(1) if match else None

    def _extract_holder_name(self, text):
        # Strategy 1: Standard Label "Name: ..."
        pattern1 = r"(?:Name|Holder|Proposer)\s*(?:of\s*Policy\s*Holder|Name)?\s*[:\-\s]*([A-Za-z\s\.]+)"
        match1 = re.search(pattern1, text, re.IGNORECASE)
        if match1 and len(match1.group(1).strip()) > 3:
             with open('debug_log.txt', 'a', encoding='utf-8') as f:
                f.write(f"Holder Pattern 1: {pattern1}\nMatch: {match1.group(1).strip()}\n")
             return match1.group(1).strip()

        # Strategy 2: Salutation "Dear Mr. ..."
        pattern2 = r"Dear\s+(?:Mr\.|Mrs\.|Ms\.|Dr\.)?\s*([A-Za-z\s\.]+)[,\n]"
        match2 = re.search(pattern2, text, re.IGNORECASE)
        result = match2.group(1).strip() if match2 else None
        
        with open('debug_log.txt', 'a', encoding='utf-8') as f:
            f.write(f"Holder Pattern 2: {pattern2}\nMatch: {result}\n")
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

