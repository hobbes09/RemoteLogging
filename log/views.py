from .models import Log
from .serializers import LogSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import create_log_from_request
from django.http import JsonResponse
from .entities import LogPostResponse
import json


class LogList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        logs = Log.objects.all()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        log, error_message = create_log_from_request(request)
        if log is None:
            log_post_response = LogPostResponse(message="Invalid Request. " + error_message, status='INACTIVE')
            return JsonResponse(json.loads(json.dumps(log_post_response.__dict__)), status=status.HTTP_400_BAD_REQUEST, content_type="application/json")

        # Check if the session is still active
        if (log.session.status == 'INACTIVE'):
            log_post_response = LogPostResponse(message="Session Expired. ", status='INACTIVE')
            return JsonResponse(json.loads(json.dumps(log_post_response.__dict__)), status=status.HTTP_200_OK, content_type="application/json")

        try:
            log.save
            log_post_response = LogPostResponse(message="Successfully created log instance. ", status='ACTIVE')
            return JsonResponse(json.loads(json.dumps(log_post_response.__dict__)), status=status.HTTP_201_CREATED, content_type="application/json")
        except Exception:
            log_post_response = LogPostResponse(message="Invalid Request Data. ", status='INACTIVE')
            return JsonResponse(json.loads(json.dumps(log_post_response.__dict__)), status=status.HTTP_400_BAD_REQUEST, content_type="application/json")



class LogDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Log.objects.get(pk=pk)
        except Log.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        log = self.get_object(pk)
        serializer = LogSerializer(log)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        return Response(data="Updating is disabled for Log for now", status=status.HTTP_400_BAD_REQUEST, content_type="text/html")
        # log = self.get_object(pk)
        # serializer = LogSerializer(log, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        log = self.get_object(pk)
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
