import os
import requests


class BaseAPI:
    def __init__(self, api_key=None, webhook_url=None, environment="sandbox"):
        """
        Initialize the API client.

        Args:
            api_key (str): API key for authentication.
            webhook_url (str): Webhook URL for notifications.
            environment (str): The environment to use ('sandbox' or 'live').
        """
        self.api_key = api_key or os.getenv("API_KEY")
        self.webhook_url = webhook_url or os.getenv("WEBHOOK_URL")

        # Set the environment (default: sandbox)
        self.environment = environment or os.getenv("API_ENV", "sandbox")

        # Define base URLs
        self.base_urls = {
            "sandbox": "https://sandbox.api.example.com",
            "live": "https://api.example.com",
        }

        # Select the base URL based on the environment
        self.base_url = self.base_urls.get(self.environment)
        if not self.base_url:
            raise ValueError(
                f"Invalid environment '{self.environment}'. Use 'sandbox' or 'live'."
            )

        if not self.api_key:
            raise ValueError("API key is required")

    def _get_headers(self):
        """Prepare headers for API requests."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _make_request(self, method, endpoint, data=None, params=None):
        """
        Make an HTTP request to the API.

        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE).
            endpoint (str): API endpoint (relative to the base URL).
            data (dict): JSON payload for the request.
            params (dict): Query parameters for the request.

        Returns:
            dict: JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = self._get_headers()
        response = requests.request(
            method, url, headers=headers, json=data, params=params
        )
        response.raise_for_status()
        return response.json()
