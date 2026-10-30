# JPMORGAN-CHASE-BANK-

This repository includes a minimal Python OAuth client for JPMorgan's client-credentials token flow.

## Prerequisites

- Python 3.10+
- A JPMorgan client ID and client secret
- Access to the JPMorgan token endpoint

## Setup

Create a local environment file from the sample:

```bash
cp .env.example .env
```

Fill in your real values in `.env`:

```dotenv
CLIENT_ID="your-client-id"
CLIENT_SECRET="your-client-secret"
SCOPE="openid profile"
```

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the client

```bash
python jpmorgan_oauth_client.py
```

This will request an access token from:

```text
https://id.payments.jpmorgan.com/am/oauth2/alpha/access_token
```

The script uses the OAuth 2.0 client credentials flow and prints the token metadata.

## Notes

- Never commit `.env` to source control.
- Keep client secrets secure and rotate them as required by your organization.
- The `scope` value is optional and depends on the permissions granted to your client.

## Example `.env` behavior

The script automatically loads `.env` if it exists in the project root.

## Minimal request flow

```python
from jpmorgan_oauth_client import get_access_token

token_data = get_access_token()
print(token_data["access_token"])
```

This is a starting point for integrating with protected JPMorgan APIs.
