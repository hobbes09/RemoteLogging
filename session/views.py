from .models import Session
from .serializers import SessionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SessionList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        return Response(data="POST request for Session is disabled", status=status.HTTP_400_BAD_REQUEST, content_type="text/html")


class SessionDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        session = self.get_object(pk)
        serializer = SessionSerializer(session)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        return Response(data="Updating is disabled for Session for now", status=status.HTTP_400_BAD_REQUEST, content_type="text/html")

    def delete(self, request, pk, format=None):
        session = self.get_object(pk)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
