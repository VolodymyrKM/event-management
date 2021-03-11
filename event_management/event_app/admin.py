from django.contrib import admin

# Register your models here.
from event_app.models import Event, EventType


class AdminEvent(admin.ModelAdmin):
    list_display = ('id', 'user', 'info', 'created_at', 'timestamp',  'event_type')
    list_filter = ('timestamp',  'event_type')


admin.site.register(Event, AdminEvent)
admin.site.register(EventType)
