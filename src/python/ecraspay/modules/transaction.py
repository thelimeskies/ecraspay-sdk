from ecraspay.base import BaseAPI


class Transaction(BaseAPI):
    """
    Transaction API
    """

    def get_transaction_details(self, transaction_ref: str) -> dict:
        """
        Fetch transaction details
        """
        return self._make_request(
            method="GET", endpoint=f"/third-party/payment/details/{transaction_ref}"
        )

    def verify_transaction(self, transaction_ref: str) -> dict:
        """
        Verify transaction
        """
        return self._make_request(
            method="GET", endpoint=f"/third-party/payment/verify/{transaction_ref}"
        )

    def get_transaction_status(self, transaction_ref: str) -> dict:
        """
        Fetch transaction status
        """
        return self._make_request(
            method="GET", endpoint=f"/third-party/payment/status/{transaction_ref}"
        )

    def cancel_transaction(self, transaction_ref: str) -> dict:
        """
        Cancel transaction
        """
        return self._make_request(
            method="GET", endpoint=f"/third-party/payment/cancel/{transaction_ref}"
        )

    def initiate_transaction(
        self,
        amount: int,
        payment_reference: str,
        customer_name: str,
        customer_email: str,
        redirect_url: str = None,
        description: str = None,
        fee_bearer: str = None,
        currency: str = "usd",
        payment_method: str = None,
        customer_phone: str = None,
        metadata: dict = None,
        **kwargs,
    ) -> dict:
        """
        Initiate a new transaction.

        Args:
            amount (int): Amount to be paid (smallest currency unit, e.g., usd for USD).
            payment_reference (str): Unique reference for the transaction.
            customer_name (str): Customer's name.
            customer_email (str): Customer's email.
            redirect_url (str, optional): URL to redirect the customer after payment.
            description (str, optional): Description of the transaction.
            fee_bearer (str, optional): Fee bearer ('customer' or 'merchant').
            currency (str, optional): Transaction currency (default: 'usd').
            payment_method (str, optional): Payment method (e.g., 'card').
            customer_phone (str, optional): Customer's phone number.
            metadata (dict, optional): Additional metadata for the transaction.
            **kwargs: Extra parameters to include in the transaction.

        Returns:
            dict: API response.
        """
        payload = {
            key: value
            for key, value in {
                "amount": amount,
                "payment_reference": payment_reference,
                "customer_name": customer_name,
                "customer_email": customer_email,
                "redirect_url": redirect_url,
                "description": description,
                "fee_bearer": fee_bearer,
                "currency": currency,
                "payment_method": payment_method,
                "customer_phone": customer_phone,
                "metadata": metadata,
            }.items()
            if value is not None
        }
        payload.update(kwargs)
        return self._make_request("POST", "checkout/initiate", data=payload)
