import requests

# DevCycle API URL and SDK configuration
DEV_CYCLE_API_KEY = 'your-api-key'
DEV_CYCLE_PROJECT_ID = 'your-project-id'

# Function to fetch feature flags from DevCycle
def get_feature_flags():
    url = f"https://api.devcycle.com/v1/projects/{DEV_CYCLE_PROJECT_ID}/flags"
    headers = {
        'Authorization': f'Bearer {DEV_CYCLE_API_KEY}',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        flags = response.json()
        return flags
    return {}

