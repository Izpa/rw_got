from django.contrib import admin

from rw_got.apps.telegram.models import User, Chat, OutgoingMessage, \
    IncomingMessage


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username')
    list_display_links = ('id',)


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'title')
    list_display_links = ('id',)


@admin.register(IncomingMessage)
class IncomingMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'chat', 'creation_date')
    list_display_links = ('id',)


@admin.register(OutgoingMessage)
class OutgoingMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'creation_date')
    list_display_links = ('id',)
