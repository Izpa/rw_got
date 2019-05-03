from django.urls import path
from django.conf import settings

from rw_got.apps.telegram.views import WebhookView

urlpatterns = [
    path(settings.TELEGRAM_BOT_WEBHOOK_PATH, WebhookView.as_view()),
]