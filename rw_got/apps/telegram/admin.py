from django.contrib import admin

from rw_got.apps.telegram.models import User, Chat, OutgoingMessage, \
    IncomingMessage


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username')
    list_display_links = ('id',)

    def has_add_permission(self, request, obj=None):
        return False


class IncomingMessageInline(admin.TabularInline):
    model = IncomingMessage
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


class OutgoingMessageInline(admin.TabularInline):
    model = OutgoingMessage
    extra = 1


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'title')
    list_display_links = ('id',)

    inlines = [IncomingMessageInline, OutgoingMessageInline]

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(IncomingMessage)
class IncomingMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'chat', 'creation_date')
    list_display_links = ('id',)

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(OutgoingMessage)
class OutgoingMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'creation_date')
    list_display_links = ('id',)
