import requests
from django.conf import settings

CHAPA_API_URL = "https://api.chapa.co/v1/transaction"

def initiate_payment(booking_reference, amount, email, first_name, last_name):
    url = f"{CHAPA_API_URL}/initialize"
    headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}

    data = {
        "amount": str(amount),
        "currency": "ETB",  # adjust if multi-currency
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "tx_ref": booking_reference,
        "callback_url": settings.CHAPA_CALLBACK_URL,
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

def verify_payment(transaction_id):
    url = f"{CHAPA_API_URL}/verify/{transaction_id}"
    headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()
