import pdfplumber
import re

class ParserService:
    def parse(self, file_path):
        text = self._extract_text(file_path)
        data = {
            'policy_number': self._extract_policy_number(text),
            'holder_name': self._extract_holder_name(text),
            'premium_amount': self._extract_premium_amount(text),
            'sum_assured': self._extract_sum_assured(text),
            'coverage_start_date': self._extract_date(text, r'Start Date'),
            'coverage_end_date': self._extract_date(text, r'End Date'),
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
        return None

    def _extract_holder_name(self, text):
        return None

    def _extract_premium_amount(self, text):
        return None

    def _extract_sum_assured(self, text):
        return None

    def _extract_date(self, text, keyword):
        return None
