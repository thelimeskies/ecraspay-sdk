package utilities

import (
    "bytes"
    "encoding/json"
    "net/http"
)

func MakeRequest(method, url string, headers map[string]string, body interface{}) (*http.Response, error) {
    var payload []byte
    if body != nil {
        payload, _ = json.Marshal(body)
    }

    req, err := http.NewRequest(method, url, bytes.NewBuffer(payload))
    if err != nil {
        return nil, err
    }

    for key, value := range headers {
        req.Header.Set(key, value)
    }

    client := &http.Client{}
    return client.Do(req)
}
