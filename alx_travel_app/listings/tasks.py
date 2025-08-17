from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_notification():
    print("Sending Notification...")
    return "Done"



@shared_task
def send_payment_confirmation_email(email, booking_reference):
    send_mail(
        "Payment Successful",
        f"Your payment for booking {booking_reference} was successful.",
        "noreply@yourapp.com",
        [email],
    )

