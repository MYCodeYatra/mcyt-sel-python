import jwt
import json
def test_jwt_decoding():
    # 1. A simulated JWT token (Usually extracted from requests or Selenium)
    # This token's payload contains: {"user_id": 105, "role": "admin", "password": "mypassword123"}
    raw_token = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        "eyJ1c2VyX2lkIjoxMDUsInJvbGUiOiJhZG1pbiIsInBhc3N3b3JkIjoibXlwYXNzd29yZDEyMyIsImV4cCI6MTUxNjIzOTAyMn0."
        "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    )
    print("\n[Security] Decoding JWT Payload...")
    # 2. Decode the payload without verifying the signature
    decoded_payload = jwt.decode(raw_token, options={"verify_signature": False})
    # Pretty print the decoded JSON
    print(json.dumps(decoded_payload, indent=2))
    assert "user_id" in decoded_payload