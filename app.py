import requests

BASE_URL = "https://postman-echo.com"

headers = {
    "User-Agent": "SEC101-Lab/1.0",
    "X-Student": "NORADT",
}

# 1) GET request
response = requests.get(
    f"{BASE_URL}/get",
    headers=headers,
    params={"course": "SEC101"},
    timeout=10,
)
print("GET status:", response.status_code)
data = response.json()
print("Headers the server received:", data["headers"])
print("Query params:", data["args"])

# 2) POST request with JSON
payload = {"name": "Norah", "topic": "AI Security"}
response = requests.post(
    f"{BASE_URL}/post",
    json=payload,
    headers=headers,
    timeout=10,
)
print("\nPOST status:", response.status_code)
print("JSON the server received:", response.json()["json"])