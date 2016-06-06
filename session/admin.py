from django.contrib import admin
from .models import Session


class SessionAdmin(admin.ModelAdmin):
    fields = ['individual', 'context', 'started_at', 'ended_at']
    list_display = ['id', 'individual', 'context', 'started_at', 'ended_at', 'created_at', 'updated_at']
    search_fields = ['id', 'individual__id', 'context']


admin.site.register(Session, SessionAdmin)