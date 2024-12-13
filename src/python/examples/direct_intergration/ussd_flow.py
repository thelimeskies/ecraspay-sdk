from urllib.error import HTTPError
from ecraspay import USSD
from ecraspay import Transaction


def generate_unique_ref():
    import random
    import string

    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


transaction = Transaction(
    api_key="ECRS-TEST-SKY13sZYcUErhEuSMxbmSicDoMLN30YskXCu8EDQRI",
    environment="sandbox",
)
ussd = USSD(
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

# Get the list of supported banks
response = ussd.get_bank_list()

bank_name = response["responseBody"][0]

# Initiate a USSD payment
try:
    response = ussd.initiate_ussd_payment(
        bank_name=bank_name, transaction_ref=transaction_reference
    )
    payment_code = response["responseBody"]["paymentCode"]
    expiration_time = response["responseBody"]["expires_in"]

    print("Payment Code: ", payment_code)
    print("Expires in: ", expiration_time)

except HTTPError as e:
    # Handle HTTP errors and print the response payload if available
    print(f"An HTTP error occurred: {e}")
    if e.response is not None:
        print("Error response payload:")
        print(e.response.json())

except Exception as e:
    # Handle other unexpected exceptions
    print(f"An unexpected error occurred: {e}")
