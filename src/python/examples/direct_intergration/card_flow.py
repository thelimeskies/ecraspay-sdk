from urllib.error import HTTPError
from ecraspay import Card
from ecraspay import Transaction
from ecraspay import card_utils


public_key_path = "path/to/public_key.pem"


def generate_unique_ref():
    import random
    import string

    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


transaction = Transaction(
    api_key="ECRS-TEST-SKY13sZYcUErhEuSMxbmSicDoMLN30YskXCu8EDQRI",
    environment="sandbox",
)
card = Card(
    api_key="ECRS-TEST-SKY13sZYcUErhEuSMxbmSicDoMLN30YskXCu8EDQRI",
    environment="sandbox",
)


# Initiate Transaction
transaction = transaction.initiate_transaction(
    amount=1000,
    payment_reference="unique_ref_1234",
    customer_name="John Doe",
    customer_email="samuelasikhalaye@gmail.com",
    currency="NGN",
    payment_method="ussd",
)

transaction_reference = transaction["responseBody"]["transactionReference"]

# initiate a card payment
try:
    response = Card.initiate_payment(
        card_payload=card_utils.encrypt_card(
            card_number="4242424242424242",
            cvv="123",
            pin="1234",
            expiration_date="12/23",
            public_key_path=public_key_path,
        ),
        transaction_ref=transaction_reference,
        device_details={"ip_address": ""},
    )
    print(response)

except HTTPError as e:
    # Handle HTTP errors and print the response payload if available
    print(f"An HTTP error occurred: {e}")
    if e.response is not None:
        print("Error response payload:")
        print(e.response.json())

except Exception as e:
    # Handle other unexpected exceptions
    print(f"An unexpected error occurred: {e}")
