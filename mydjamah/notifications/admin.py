from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'receiver',
        'sender',
        'message',
        'is_read',
        'created_at'  
    )
    list_filter = ('is_read', 'created_at')  
    search_fields = ('message', 'receiver__email', 'sender__email')
    ordering = ('-created_at',)  
