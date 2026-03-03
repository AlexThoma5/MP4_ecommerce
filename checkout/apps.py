from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration for the Checkout application.

    The `ready` method imports signal handlers to ensure they are
    connected when the app is loaded.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
