import requests
from urllib.parse import urlparse, parse_qs

# Hex-encoded URL
hex_url = "68747470733a2f2f6c612e64726d6c6976652e6e65742f74702f7a65652d7a656574616d696c2e6d337538"

# Decode it back to the original URL
initial_url = bytes.fromhex(hex_url).decode()

try:
    # Send GET request and follow redirects
    response = requests.get(initial_url, allow_redirects=True)
    final_url = response.url
    print(f"Final URL: {final_url}")

    # Extract 'hdntl' parameter
    parsed_url = urlparse(final_url)
    query_params = parse_qs(parsed_url.query)
    hdntl_value = query_params.get('hdntl', [None])[0]

    if hdntl_value:
        with open('cookie.txt', 'w') as file:
            file.write(hdntl_value)
        print("Cookie saved to cookie.txt")
    else:
        print("hdntl parameter not found.")

except requests.RequestException as e:
    print(f"Error: {e}")
