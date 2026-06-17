import json
from resilient import SimpleClient

RESILIENT_URL = "https://your-resilient-instance.com"
ORG_NAME = "your_org"
client = SimpleClient(base_url=RESILIENT_URL, org_name=ORG_NAME)
client.set_api_key(api_key_id="your_key_id", api_key_secret="your_key_secret")

incidents = client.get("/incidents")
print(json.dumps(incidents, indent=2))
