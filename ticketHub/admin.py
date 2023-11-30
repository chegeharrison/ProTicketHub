from django.contrib import admin
from .models import EventDb


class EventDbAdmin(admin.ModelAdmin):
    list_display = ['Event_title', 'Date', 'Time', 'Location', 'approved']
    list_filter = ['approved']

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.approved:
            # Disable all fields if the event is approved
            return [field.name for field in self.opts.fields]
        return []

    def has_delete_permission(self, request, obj=None):
        # Disable delete permission if the event is approved
        return not (obj and obj.approved)

admin.site.register(EventDb, EventDbAdmin)

