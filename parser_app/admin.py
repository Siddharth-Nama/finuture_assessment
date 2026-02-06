from django.contrib import admin
from .models import InsuranceDocument, ExtractedData

admin.site.register(InsuranceDocument)
admin.site.register(ExtractedData)
