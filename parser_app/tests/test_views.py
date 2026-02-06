import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
def test_upload_document():
    client = APIClient()
    file = SimpleUploadedFile("test.pdf", b"file_content", content_type="application/pdf")
    response = client.post('/api/upload/', {'file': file}, format='multipart')
    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.data
    assert 'file' in response.data
