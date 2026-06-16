import requests
import pytest
def get_parsed_csp(url: str) -> dict:
    """Fetches the CSP header and parses it into a dictionary."""
    response = requests.get(url)
    # 1. Ensure the header exists
    csp_raw = response.headers.get("Content-Security-Policy")
    assert csp_raw is not None, f"CSP header missing on {url}"
    # 2. Parse the string into a dictionary
    csp_dict = {}
    # Split by semicolon to get directives
    directives = [d.strip() for d in csp_raw.split(";") if d.strip()]
    for directive in directives:
        # The first word is the key, the rest are values
        parts = directive.split(" ")
        key = parts[0]
        values = parts[1:] if len(parts) > 1 else []
        csp_dict[key] = values
    return csp_dict