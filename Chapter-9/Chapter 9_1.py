# Pseudo-code for Radiant connector API call
import requests

api_token = "your_radiant_api_token"
headers = {"Authorization": f"Bearer {api_token}"}
response = requests.get("https://api.radiantsecurity.ai/v1/incidents", headers=headers)
incidents = response.json()
