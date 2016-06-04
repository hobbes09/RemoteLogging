from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'slug', 'company_name', 'app_name', 'package_name', 'created_at', 'updated_at')

