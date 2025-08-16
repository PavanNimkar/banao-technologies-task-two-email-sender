from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import JsonResponse


@api_view(["GET", "POST"])
def send_email_view(request):
    receiver = request.data.get("receiver_email")
    subject = request.data.get("subject")
    body = request.data.get("body_text")

    if not receiver or not subject or not body:
        return Response(
            {
                "status": "error",
                "message": "receiver_email, subject and body_text are required",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        send_mail(
            subject=subject,
            message=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[receiver],
            fail_silently=False,
        )
        return Response(
            {
                "status": "success",
                "message": "Email sent successfully!",
            },
            status=status.HTTP_200_OK,
        )
    except BadHeaderError:
        return Response(
            {"status": "error", "message": "Invalid header found."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as e:
        return Response(
            {"status": "error", "message": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
