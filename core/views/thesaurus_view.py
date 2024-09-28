from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.thesaurus import Thesaurus
from core.serializers.thesaurus_serializer import ThesaurusSerializer

class ThesaurusView(APIView):
    def get(self, request):
        thesaurus = Thesaurus.objects.first()
        if thesaurus:
            serializer = ThesaurusSerializer(thesaurus)
            return Response(serializer.data)
        return Response({'error': 'Thesaurus not found'}, status=status.HTTP_404_NOT_FOUND)
