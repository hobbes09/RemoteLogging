from django.contrib import admin
from .models import Client
from individual.models import Individual

class IndividualInline(admin.StackedInline):
    model = Individual
    extra = 2


class ClientAdmin(admin.ModelAdmin):
    fields = ['company_name', 'app_name', 'package_name']
    list_display = ['id', 'slug', 'company_name', 'app_name', 'package_name', 'created_at', 'updated_at']
    list_filter = ['company_name', 'app_name', 'package_name']
    search_fields = ['id', 'slug', 'company_name', 'app_name', 'package_name']
    inlines = [IndividualInline]

admin.site.register(Client, ClientAdmin)