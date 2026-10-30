# JPMORGAN-CHASE-BANK-

This repository provides a minimal starting point for obtaining an OAuth access token from JPMorgan's `id.payments.jpmorgan.com` token endpoint.

## Example: request a token using client credentials

Set your credentials before running the request:

```bash
export CLIENT_ID="your-client-id"
export CLIENT_SECRET="your-client-secret"
export SCOPE="openid profile"
```

Then send the request:

```bash
curl -X POST "https://id.payments.jpmorgan.com/am/oauth2/alpha/access_token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "grant_type=client_credentials" \
  --data-urlencode "client_id=${CLIENT_ID}" \
  --data-urlencode "client_secret=${CLIENT_SECRET}" \
  --data-urlencode "scope=${SCOPE}"
```

The response will be JSON similar to:

```json
{
  "access_token": "...",
  "token_type": "Bearer",
  "expires_in": 3599
}
```

You can extract the access token with:

```bash
curl -s -X POST "https://id.payments.jpmorgan.com/am/oauth2/alpha/access_token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "grant_type=client_credentials" \
  --data-urlencode "client_id=${CLIENT_ID}" \
  --data-urlencode "client_secret=${CLIENT_SECRET}" \
  --data-urlencode "scope=${SCOPE}" | jq -r '.access_token'
```

## Notes

- Replace the example values with your own credentials.
- Ensure the requested scope matches the permissions granted to your client.
- Treat all tokens as sensitive data and do not commit them to source control.
