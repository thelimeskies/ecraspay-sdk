# ECRASPAY Python SDK

ECRASPAY SDK provides a convenient and Pythonic way to interact with the ECRASPAY API for managing payments and transactions. This package simplifies initiating and managing payments, such as card payments, USSD, bank transfers, and transaction verification.

---

## Features
- **Direct integration with the ECRASPAY API:**
  - **Transaction Management**:
    - Fetch transaction details and status.
    - Cancel transactions.
    - Verify transactions.

  - **Card Payments**:
    - Initiate card payments.
    - Submit and resend OTPs.
    - Fetch card transaction details.
    - Verify card payments.

  - **USSD Payments**:
    - Initiate USSD payments.
    - Retrieve a list of supported banks for USSD payments.

  - **Bank Transfers**:
    - Initialize bank transfers by requesting bank account details.

- **Checkout Payments**:
  - Initiate checkout transactions.
  - Verify checkout transactions.


---

## Installation

### Prerequisites

- Python 3.6 or later.

### Installation via pip

```bash
pip install ecraspay-py
```

---

## Usage

### Initialize the EcrasPay client

#### - Checkouts Payments

```python
```

## TODO

- [ ] Finish Documentation
- [ ] Add examples
- [ ] Finish Tests
- [ ] Write and Document all Utility functions for the SDK(Django, Flask, FastAPI, Pure Python) - e.g. `get_device_details`, `encrypt_card`, `clean_phone_number`, `clean_amount`, `clean_email`, `clean_name`, `clean_transaction_id`.
