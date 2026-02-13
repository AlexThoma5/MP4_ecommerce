from django.http import HttpResponse


class StripeWebhookHandler:
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unkown/unexpected webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
