import pytest
from parser_app.models import InsuranceDocument, ExtractedData

@pytest.mark.django_db
def test_create_document():
    doc = InsuranceDocument.objects.create(file="test.pdf")
    assert doc.id is not None
    assert doc.file.name == "test.pdf"

@pytest.mark.django_db
def test_create_extracted_data():
    doc = InsuranceDocument.objects.create(file="test.pdf")
    data = ExtractedData.objects.create(
        document=doc,
        policy_number="12345",
        holder_name="John Doe"
    )
    assert data.policy_number == "12345"
    assert data.document == doc
