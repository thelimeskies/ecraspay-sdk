package ecraspay

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"time"
)

// BaseAPI is the core structure for making API requests.
type BaseAPI struct {
	APIKey      string
	Environment string
	BaseURL     string
	Client      *http.Client
}

// NewBaseAPI initializes a new BaseAPI instance.
func NewBaseAPI(apiKey, environment string) *BaseAPI {
	baseURL := "https://sandbox.api.example.com"
	if environment == "live" {
		baseURL = "https://api.example.com"
	}
	return &BaseAPI{
		APIKey:      apiKey,
		Environment: environment,
		BaseURL:     baseURL,
		Client:      &http.Client{Timeout: 10 * time.Second},
	}
}

// MakeRequest performs an HTTP request and handles the response.
func (b *BaseAPI) MakeRequest(method, endpoint string, payload interface{}) (map[string]interface{}, error) {
	url := fmt.Sprintf("%s%s", b.BaseURL, endpoint)

	// Prepare request body
	var body []byte
	if payload != nil {
		jsonData, err := json.Marshal(payload)
		if err != nil {
			return nil, fmt.Errorf("failed to serialize payload: %w", err)
		}
		body = jsonData
	}

	// Create HTTP request
	req, err := http.NewRequest(method, url, bytes.NewBuffer(body))
	if err != nil {
		return nil, fmt.Errorf("failed to create request: %w", err)
	}

	// Set headers
	req.Header.Set("Authorization", fmt.Sprintf("Bearer %s", b.APIKey))
	req.Header.Set("Content-Type", "application/json")

	// Send request
	resp, err := b.Client.Do(req)
	if err != nil {
		return nil, fmt.Errorf("request failed: %w", err)
	}
	defer resp.Body.Close()

	// Read and parse response body
	responseBody, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("failed to read response body: %w", err)
	}

	if resp.StatusCode >= 400 {
		return nil, fmt.Errorf("HTTP error %d: %s", resp.StatusCode, string(responseBody))
	}

	var result map[string]interface{}
	if err := json.Unmarshal(responseBody, &result); err != nil {
		return nil, fmt.Errorf("failed to parse JSON response: %w", err)
	}
	return result, nil
}
