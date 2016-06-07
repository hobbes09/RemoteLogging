from .models import Individual
from session.models import Session
from .serializers import IndividualSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from client.models import Client
from .utils import create_individual_from_request
from .entities import IndividualStatus
from django.http import JsonResponse
import json


def get_individual_logging_status(request, ext_id, format=None):
    exception = None
    individual_status = None
    try:
        individual = Individual.objects.get(external_id=ext_id)
    except Exception as e:
        individual = None
        exception = e

    if(individual is None):
        return JsonResponse({"error": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST, content_type="application/json")

    sessions = Session.objects.filter(individual=individual, status='ACTIVE').order_by('-updated_at')

    if(len(sessions) > 0):
        session = sessions[0]
        individual_status = IndividualStatus(individual_id=ext_id, session_id=session.id, status=session.status, type=session.type)
    else:
        individual_status = IndividualStatus(individual_id=ext_id, session_id=None, status='INACTIVE', type=None)

    return JsonResponse(json.loads(json.dumps(individual_status.__dict__)), status=status.HTTP_200_OK, content_type="application/json")



def get_client_id_from_slug(slug):
    try:
        client = Client.objects.get(slug=slug)
        return client.id
    except Client.DoesNotExist:
        return ''

class IndividualList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        individuals = Individual.objects.all()
        serializer = IndividualSerializer(individuals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        individual = create_individual_from_request(request)
        if individual is None:
            return Response(data="Invalid Request", status=status.HTTP_400_BAD_REQUEST, content_type="text/html")

        try:
            individual.save
            return Response(data="Successfully created individual instance", status=status.HTTP_201_CREATED, content_type="text/html")
        except Exception:
            return Response(data="Invalid Request Data", status=status.HTTP_400_BAD_REQUEST, content_type="text/html")


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
        return Response(data="Updating is disabled for Individuals for now", status=status.HTTP_400_BAD_REQUEST, content_type="text/html")
        # individual = self.get_object(ext_id)
        # serializer = IndividualSerializer(individual, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ext_id, format=None):
        individual = self.get_object(ext_id)
        individual.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
