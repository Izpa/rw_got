from django.contrib import admin

from rw_got.apps.telegram.models import User, Chat, OutgoingMessage, \
    IncomingMessage


class ReadOnlyAdminMixin(object):
    """Disables all editing capabilities."""
    change_form_template = "admin/view.html"

    def __init__(self, *args, **kwargs):
        super(ReadOnlyAdminMixin, self).__init__(*args, **kwargs)
        self.readonly_fields = self.model._meta.get_all_field_names()

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin, ReadOnlyAdminMixin):
    list_display = ('id', 'first_name', 'last_name', 'username')
    list_display_links = ('id',)
    readonly_fields = ('id', 'external_id', )


class IncomingMessageInline(admin.TabularInline, ReadOnlyAdminMixin):
    model = IncomingMessage
    extra = 0
    can_delete = False


class OutgoingMessageInline(admin.TabularInline, ReadOnlyAdminMixin):
    model = OutgoingMessage
    extra = 1
    can_delete = False


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin, ReadOnlyAdminMixin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'title')
    list_display_links = ('id',)

    inlines = [IncomingMessageInline, OutgoingMessageInline]


@admin.register(IncomingMessage)
class IncomingMessageAdmin(admin.ModelAdmin, ReadOnlyAdminMixin):
    list_display = ('id', 'text', 'user', 'chat', 'creation_date')
    list_display_links = ('id',)


@admin.register(OutgoingMessage)
class OutgoingMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'creation_date')
    list_display_links = ('id',)

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return self.model._meta.get_all_field_names()
