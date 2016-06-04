from rest_framework import serializers
from .models import Individual

class IndividualSerializer(serializers.ModelSerializer):
    client_slug = serializers.CharField(source='client.slug', read_only=True)

    class Meta:
        model = Individual
        fields = ('id', 'external_id', 'client_slug', 'os', 'version', 'created_at', 'updated_at')

