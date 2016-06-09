from django.contrib import admin
from .models import Individual
from log.models import Log

class LogInline(admin.StackedInline):
    model = Log
    extra = 2


class IndividualAdmin(admin.ModelAdmin):
    fields = ['external_id', 'client', 'os', 'version']
    list_display = ['id', 'external_id', 'client', 'os', 'version', 'created_at', 'updated_at']
    list_filter = ['client', 'os', 'version']
    search_fields = ['id', 'external_id', 'client__slug', 'os', 'version']
    inlines = [LogInline]

admin.site.register(Individual, IndividualAdmin)
