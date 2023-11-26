from django.contrib import admin
from .models import EventDb


class EventDbAdmin(admin.ModelAdmin):
    list_display = ['Event_title', 'Date', 'Time', 'Location', 'approved']
    list_filter = ['approved']

    def get_readonly_fields(self, request, obj=None):
        return []  # Allow editing all fields, including 'approved'
admin.site.register(EventDb, EventDbAdmin)

