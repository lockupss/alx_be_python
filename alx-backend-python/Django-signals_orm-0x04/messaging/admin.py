from django.contrib import admin
from .models import Message, Notification, MessageHistory

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'timestamp', 'edited', 'read')
    search_fields = ('sender__username', 'receiver__username', 'content')
    list_filter = ('edited', 'read', 'timestamp')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'created_at', 'is_read')
    search_fields = ('user__username',)
    list_filter = ('is_read', 'created_at')

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'edited_at')
    search_fields = ('message__content',)
    list_filter = ('edited_at',)
