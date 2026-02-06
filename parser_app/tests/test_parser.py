import pytest
from parser_app.services import ParserService

def test_extract_policy_number():
    parser = ParserService()
    text = "Policy No: P-123456"
    assert parser._extract_policy_number(text) == "P-123456"

def test_extract_dates():
    parser = ParserService()
    text = "Start Date: 01/01/2023 End Date: 31/12/2023"
    assert parser._extract_date(text, "Start Date") == "01/01/2023"
    assert parser._extract_date(text, "End Date") == "31/12/2023"

def test_extract_amounts():
    parser = ParserService()
    text = "Premium: Rs. 1,00,000 Sum Assured: INR 50,00,000"
    assert parser._extract_premium_amount(text) == "1,00,000"
    assert parser._extract_sum_assured(text) == "50,00,000"

def test_extract_holder_name():
    parser = ParserService()
    text = "Name: John Doe"
    assert parser._extract_holder_name(text) == "John Doe"
