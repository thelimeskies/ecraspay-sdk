import pytest
from unittest.mock import patch
from ecraspay.base import BaseAPI


class TestBaseAPI:
    """
    Test suite for the BaseAPI class.

    This class contains tests for the BaseAPI class, ensuring that its methods
    and initialization work as expected under various conditions.

    Test Cases:
        - Initialization with valid and invalid inputs.
        - Handling of missing API key.
        - Handling of invalid environments.
        - Making API requests and ensuring the correct behavior.
    """

    @pytest.fixture
    def api_instance(self):
        """
        Fixture for initializing a BaseAPI instance.

        Returns:
            BaseAPI: A BaseAPI instance with a test API key and sandbox environment.
        """
        return BaseAPI(api_key="test_key", environment="sandbox")

    def test_init(self, api_instance):
        """
        Test the initialization of the BaseAPI class.

        Verifies that the API key, environment, and base URL are correctly set during initialization.

        Args:
            api_instance (BaseAPI): A fixture providing a pre-initialized BaseAPI instance.
        """
        assert api_instance.api_key == "test_key"
        assert api_instance.environment == "sandbox"
        assert api_instance.base_url == "https://sandbox.api.example.com"

    def test_invalid_environment(self):
        """
        Test that an invalid environment raises a ValueError.

        Ensures that only 'sandbox' or 'live' are allowed as valid environments.
        """
        with pytest.raises(ValueError):
            BaseAPI(api_key="test_key", environment="invalid")

    def test_missing_api_key(self):
        """
        Test that a missing API key raises a ValueError.

        Ensures that the API key is required during initialization.
        """
        with pytest.raises(ValueError):
            BaseAPI()

    @patch("requests.request")
    def test_make_request(self, mock_request, api_instance):
        """
        Test the _make_request method of the BaseAPI class.

        Verifies that the method correctly makes HTTP requests and processes the response.

        Args:
            mock_request (MagicMock): A mocked version of the `requests.request` method.
            api_instance (BaseAPI): A fixture providing a pre-initialized BaseAPI instance.
        """
        mock_response = mock_request.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "success"}

        response = api_instance._make_request("GET", "test-endpoint")
        assert response == {"message": "success"}

        mock_request.assert_called_once_with(
            "GET",
            "https://sandbox.api.example.com/test-endpoint",
            headers={
                "Authorization": "Bearer test_key",
                "Content-Type": "application/json",
            },
            json=None,
            params=None,
        )
