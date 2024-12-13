package ecraspay

import "fmt"

type APIError struct {
    Code    int
    Message string
}

func (e *APIError) Error() string {
    return fmt.Sprintf("APIError: Code=%d, Message=%s", e.Code, e.Message)
}
