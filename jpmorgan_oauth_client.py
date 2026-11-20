import os
import sys

import requests
from dotenv import load_dotenv


TOKEN_URL = "https://id.payments.jpmorgan.com/am/oauth2/alpha/access_token"


def get_access_token() -> dict:
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    scope = os.getenv("SCOPE")

    if not client_id or not client_secret:
        raise RuntimeError("CLIENT_ID and CLIENT_SECRET must be set in .env")

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    if scope:
        data["scope"] = scope

    response = requests.post(
        TOKEN_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=data,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def main() -> None:
    try:
        token_data = get_access_token()

        # Print metadata only; never print the access token itself.
        safe_metadata = {
            key: value
            for key, value in token_data.items()
            if key not in {"access_token", "refresh_token", "client_secret"}
        }
        print(safe_metadata)

    except requests.HTTPError as error:
        print(f"Token request failed: {error}", file=sys.stderr)
        if error.response is not None:
            print(error.response.text, file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
