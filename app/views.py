from rest_framework import status
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView

from app.models import Skin
from app.serializers import SkinSerializer

class SkinList(APIView):
    """
    Listar ou criação de posts
    """
    def get(self):
        skins = Skin.objects.all()
        serializer = SkinSerializer(skins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SkinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SkinDetail(APIView):
    """
    Receber, atualizar ou delete de posts
    """
    def get_object(self, pk):
        try:
            return Skin.objects.get(pk=pk)
        except Skin.DoesNotExist:
            raise Http404

    def get(self, pk):
        skin = self.get_object(pk)
        serializer = SkinSerializer(skin)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        skin = self.get_object(pk)
        serializer = SkinSerializer(skin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        skin = self.get_object(pk)
        skin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    