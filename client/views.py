from .models import Client
from .serializers import ClientSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ClientList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, slug):
        try:
            return Client.objects.get(slug=slug)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        client = self.get_object(slug)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        client = self.get_object(slug)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        client = self.get_object(slug)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
