from ecraspay.base import BaseAPI


class USSD(BaseAPI):
    def initiate_ussd_payment(self, bank_name: str, transaction_ref: str) -> dict:
        payload = {
            "bank_name": bank_name,
        }

        return self._make_request(
            method="POST",
            endpoint=f"/payment/ussd/request-ussd-code/{transaction_ref}",
            payload=payload,
        )

    def get_bank_list(self) -> dict:
        return self._make_request(
            method="GET",
            endpoint="/third-party/payment/ussd/supported-banks",
        )
