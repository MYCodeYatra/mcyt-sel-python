import requests
def test_api_security_headers():
    # 1. Make an HTTP GET request to the environment
    response = requests.get("https://github.com")
    headers = response.headers
    print("\n[Security] Analyzing HTTP Response Headers...")
    # 2. Assert Strict-Transport-Security (HSTS)
    assert "Strict-Transport-Security" in headers, "HSTS Header is MISSING!"
    print(f"✅ HSTS: {headers['Strict-Transport-Security']}")
    # 3. Assert X-Frame-Options (Clickjacking Protection)
    assert "X-Frame-Options" in headers, "X-Frame-Options is MISSING!"
    print(f"✅ X-Frame-Options: {headers['X-Frame-Options']}")
    # 4. Assert X-Content-Type-Options
    assert "X-Content-Type-Options" in headers, "X-Content-Type-Options is MISSING!"
    print(f"✅ X-Content-Type-Options: {headers['X-Content-Type-Options']}")
    # 5. Assert Content-Security-Policy
    assert "Content-Security-Policy" in headers, "CSP Header is MISSING!"
    print(f"✅ CSP: {headers['Content-Security-Policy'][:50]}...") # Truncating for readability