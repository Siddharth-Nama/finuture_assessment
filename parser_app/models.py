from django.db import models

class InsuranceDocument(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document {self.id} - {self.uploaded_at}"

class ExtractedData(models.Model):
    document = models.ForeignKey(InsuranceDocument, on_delete=models.CASCADE, related_name='extracted_data')
    policy_number = models.CharField(max_length=100, null=True, blank=True)
    holder_name = models.CharField(max_length=255, null=True, blank=True)
    premium_amount = models.CharField(max_length=50, null=True, blank=True)
    sum_assured = models.CharField(max_length=50, null=True, blank=True)
    coverage_start_date = models.DateField(null=True, blank=True)
    coverage_end_date = models.DateField(null=True, blank=True)
    raw_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data for Document {self.document.id}"
