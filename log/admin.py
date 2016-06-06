from django.contrib import admin
from .models import Log

class LogAdmin(admin.ModelAdmin):
    fields = ['type', 'individual', 'body']
    list_display = ['id', 'type', 'individual', 'body', 'created']
    list_filter = ['type']
    search_fields = ['id', 'type', 'individual__id', 'individual__external_id', 'body']


admin.site.register(Log, LogAdmin)