from django.contrib import admin
from .models import Session
from log.models import Log

# class LogInline(admin.StackedInline):
#     model = Log
#     extra = 2
#
# class SessionAdmin(admin.ModelAdmin):
#     fields = ['individual', 'context', 'status', 'type', 'started_at', 'ended_at']
#     list_display = ['id', 'individual', 'context', 'type', 'started_at', 'ended_at', 'status', 'created_at', 'updated_at']
#     list_filter = ['status',  'type']
#     search_fields = ['id', 'individual__id', 'individual__external_id', 'context', 'status',  'type']
#     inlines = [LogInline]
#
#
# admin.site.register(Session, SessionAdmin)


class SessionAdmin(admin.ModelAdmin):
    fields = ['individual', 'context', 'status', 'type', 'started_at', 'ended_at']
    list_display = ['id', 'individual', 'context', 'type', 'started_at', 'ended_at', 'status', 'created_at', 'updated_at']
    list_filter = ['status',  'type']
    search_fields = ['id', 'individual__id', 'individual__external_id', 'context', 'status',  'type']

admin.site.register(Session, SessionAdmin)