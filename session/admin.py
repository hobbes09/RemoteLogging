from django.contrib import admin
from .models import Session


class SessionAdmin(admin.ModelAdmin):
    fields = ['individual', 'context', 'status', 'started_at', 'ended_at']
    list_display = ['id', 'individual', 'context', 'started_at', 'ended_at', 'status', 'created_at', 'updated_at']
    list_filter = ['status']
    search_fields = ['id', 'individual__id', 'individual__external_id', 'context', 'status']


admin.site.register(Session, SessionAdmin)