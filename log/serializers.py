from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    individual_ext_id = serializers.CharField(source='individual.external_id', read_only=True)
    session_id = serializers.CharField(source='session.id', read_only=True)

    class Meta:
        model = Log
        fields = ('id', 'created', 'body', 'type', 'individual_ext_id', 'session_id')

