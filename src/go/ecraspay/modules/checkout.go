package ecraspay

import (
	"errors"
	"fmt"
)


type Checkout struct {
	BaseAPI *BaseAPI
}

func NewCheckout(apiKey, environment string) *Checkout {
	return &Checkout{BaseAPI: NewBaseAPI(apiKey, environment)}
}

func (c *Checkout) InitiateTransaction(
	amount int,
	paymentReference string,
	customerName string,
	customerEmail string,
	redirectURL string,
	description string,
	feeBearer string,
	currency string,
	paymentMethod string,
	customerPhone string,
	metadata map[string]interface{},
	extraParams map[string]interface{},
) (map[string]interface{}, error) {
	if amount <= 0 {
		return nil, errors.New("amount must be greater than 0")
	}
	if paymentReference == "" {
		return nil, errors.New("paymentReference is required")
	}
	if customerName == "" {
		return nil, errors.New("customerName is required")
	}
	if customerEmail == "" {
		return nil, errors.New("customerEmail is required")
	}

	payload := map[string]interface{}{
		"amount":                amount,
		"paymentReference":      paymentReference,
		"customerName":          customerName,
		"customerEmail":         customerEmail,
		"redirectUrl":           redirectURL,
		"description":           description,
		"feeBearer":             feeBearer,
		"currency":              currency,
		"paymentMethods":        paymentMethod,
		"customerPhoneNumber":   customerPhone,
		"metadata":              metadata,
	}

	for key, value := range extraParams {
		payload[key] = value
	}

	return c.BaseAPI.MakeRequest("POST", "/payment/initiate", payload)
}

func (c *Checkout) VerifyTransaction(transactionID string) (map[string]interface{}, error) {
	// Validate required fields
	if transactionID == "" {
		return nil, errors.New("transactionID is required")
	}

	// Make the API request
	endpoint := fmt.Sprintf("/payment/transaction/verify/%s", transactionID)
	return c.BaseAPI.MakeRequest("GET", endpoint, nil)
}
