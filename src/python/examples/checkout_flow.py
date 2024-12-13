from requests import HTTPError
from ecraspay import Checkout

# Initialize the Checkout API
api = Checkout(
    api_key="ECRS-TEST-SKY13sZYcUErhEuSMxbmSicDoMLN30YskXCu8EDQRI",
    environment="sandbox",
)

try:
    # Step 1: Initiate a checkout session
    response = api.initiate_transaction(
        amount=1000,
        payment_reference="unique_ref_1234",
        customer_name="John Doe",
        customer_email="samuelasikhalaye@gmail.com",
    )

    # Extract transaction details from the response
    transaction_reference = response["responseBody"]["transactionReference"]
    checkout_url = response["responseBody"]["checkoutUrl"]

    print("Transaction initiated successfully!")
    print(f"Transaction Reference: {transaction_reference}")
    print(f"Checkout URL: {checkout_url}")

    # Step 2: Verify the transaction
    verify_transaction = api.verify_transaction(transaction_reference)
    print("Transaction verification successful!")
    print(verify_transaction)

except HTTPError as e:
    # Handle HTTP errors and print the response payload if available
    print(f"An HTTP error occurred: {e}")
    if e.response is not None:
        print("Error response payload:")
        print(e.response.json())

except Exception as e:
    # Handle other unexpected exceptions
    print(f"An unexpected error occurred: {e}")
