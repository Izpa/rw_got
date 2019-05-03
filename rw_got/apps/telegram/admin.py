from django.contrib import admin

from rw_got.apps.telegram.models import User, Chat, OutgoingMessage, \
    IncomingMessage


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(IncomingMessage)
class IncomingMessageAdmin(admin.ModelAdmin):
    pass


@admin.register(OutgoingMessage)
class OutgoingMessageAdmin(admin.ModelAdmin):
    pass
