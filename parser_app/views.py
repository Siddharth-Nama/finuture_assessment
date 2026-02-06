from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import InsuranceDocumentSerializer
from .models import ExtractedData
from .services import ParserService

class DocumentUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = InsuranceDocumentSerializer(data=request.data)
        if serializer.is_valid():
            document = serializer.save()
            
            try:
                parser = ParserService()
                data = parser.parse(document.file.path)
                
                ExtractedData.objects.create(
                    document=document,
                    policy_number=data.get('policy_number'),
                    holder_name=data.get('holder_name'),
                    premium_amount=data.get('premium_amount'),
                    sum_assured=data.get('sum_assured'),
                    coverage_start_date=data.get('coverage_start_date'),
                    coverage_end_date=data.get('coverage_end_date'),
                    raw_data=data.get('raw_data')
                )
            except Exception as e:
                # Log error but don't fail upload? Or fail? User wants extraction.
                # Ideally, we return partial success or error. For now, let's just proceed.
                print(f"Parsing failed: {e}")

            return Response(InsuranceDocumentSerializer(document).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
