from rest_framework import serializers
from .models import InsuranceDocument, ExtractedData

class ExtractedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedData
        fields = '__all__'

class InsuranceDocumentSerializer(serializers.ModelSerializer):
    extracted_data = ExtractedDataSerializer(many=True, read_only=True)

    class Meta:
        model = InsuranceDocument
        fields = ['id', 'file', 'uploaded_at', 'extracted_data']
