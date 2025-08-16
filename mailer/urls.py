from django.urls import path
from .views import send_email_view
from .views import test_email

urlpatterns = [
    path("send-email/", send_email_view, name="send-email"),
]
