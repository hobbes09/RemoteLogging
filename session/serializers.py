from rest_framework import serializers
from .models import Session

class SessionSerializer(serializers.ModelSerializer):
    individual_id = serializers.CharField(source='individual.id', read_only=True)

    class Meta:
        model = Session
        fields = ('id', 'individual_id', 'context', 'status', 'type', 'started_at', 'ended_at', 'created_at', 'updated_at')

