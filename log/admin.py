from django.contrib import admin
from .models import Log

class LogAdmin(admin.ModelAdmin):
    fields = ['type', 'individual', 'session', 'body']
    list_display = ['id', 'type', 'individual', 'session', 'body', 'created']
    list_filter = ['type']
    search_fields = ['id', 'type', 'individual__id', 'individual__external_id', 'session__id', 'body']


admin.site.register(Log, LogAdmin)