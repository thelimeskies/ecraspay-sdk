from django.dispatch import Signal


webhook_received = Signal(providing_args=["request", "event"])