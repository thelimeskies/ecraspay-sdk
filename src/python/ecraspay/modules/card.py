from ecraspay.base import BaseAPI


class Card(BaseAPI):
    def initiate_payment(
        self, card_payload: str, transaction_ref: str, device_details: dict
    ) -> dict:
        payload = {
            "payload": card_payload,
            "transactionReference": transaction_ref,
            "deviceDetails": device_details,
        }

        return self._make_request(
            method="POST",
            endpoint="/third-party/payment/cards/initialize",
            payload=payload,
        )

    def submit_otp(self, otp: str, gateway_ref: str) -> dict:
        payload = {
            "otp": otp,
            "gatewayReference": gateway_ref,
        }

        return self._make_request(
            method="POST",
            endpoint="/third-party/payment/cards/otp/submit/",
            payload=payload,
        )

    def resend_otp(
        self,
        gateway_ref: str,
    ) -> dict:
        payload = {
            "gatewayReference": gateway_ref,
        }

        return self._make_request(
            method="POST",
            endpoint="/third-party/payment/cards/otp/resend/",
            payload=payload,
        )

    def get_card_details(self, transaction_ref: str) -> dict:
        return self._make_request(
            method="GET",
            endpoint=f"/third-party/payment/cards/details/{transaction_ref}",
        )

    def verify_card_payment(self, transaction_ref: str) -> dict:
        payload = {
            "transactionReference": transaction_ref,
        }

        return self._make_request(
            method="POST",
            endpoint="/third-party/payment/cards/verify/",
            payload=payload,
        )
