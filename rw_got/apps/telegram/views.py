from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from rw_got.apps.telegram.bot import Bot


class WebhookView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WebhookView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        message = request.body.decode()
        Bot().accept_message(message)
