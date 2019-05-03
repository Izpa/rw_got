from django.views import View

from rw_got.apps.telegram.bot import Bot


class WebhookView(View):

    def post(self, request):
        Bot().accept_message(request.body)
