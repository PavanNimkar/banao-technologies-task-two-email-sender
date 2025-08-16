from django.urls import path
from .views import send_email_view
from .views import test_email

urlpatterns = [
    path("send-email/", send_email_view, name="send-email"),
    path("test-email/", test_email, name="test-email"),
]
