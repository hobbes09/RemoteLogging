from .models import Log
from .serializers import LogSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import create_log_from_request


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
            return Response(data="Invalid Request." + error_message, status=status.HTTP_400_BAD_REQUEST, content_type="text/html")

        try:
            log.save
            return Response(data="Successfully created log instance", status=status.HTTP_201_CREATED, content_type="text/html")
        except Exception:
            return Response(data="Invalid Request Data", status=status.HTTP_400_BAD_REQUEST, content_type="text/html")



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
