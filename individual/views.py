from .models import Individual
from .serializers import IndividualSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class IndividualList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        individuals = Individual.objects.all()
        serializer = IndividualSerializer(individuals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IndividualSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IndividualDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, ext_id):
        try:
            return Individual.objects.get(external_id=ext_id)
        except Individual.DoesNotExist:
            raise Http404

    def get(self, request, ext_id, format=None):
        individual = self.get_object(ext_id)
        serializer = IndividualSerializer(individual)
        return Response(serializer.data)

    def put(self, request, ext_id, format=None):
        individual = self.get_object(ext_id)
        serializer = IndividualSerializer(individual, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ext_id, format=None):
        individual = self.get_object(ext_id)
        individual.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
