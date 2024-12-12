from ecraspay.base import BaseAPI


class BankTransfer(BaseAPI):
    def initialize_bank_transfer(self, transaction_ref: str) -> dict:
        return self._make_request(
            method="GET",
            endpoint=f"/third-party/payment/bank-transfer/request-bank-account/{transaction_ref}",
        )
