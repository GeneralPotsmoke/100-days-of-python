#### Day 38: Build a Workout Tracking App that Talks to Google Sheets!
**Challenge:** Create a program that logs your workouts to Google Sheets using the Sheety API.

```python
import requests
import os
from datetime import datetime

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
SHEET_TOKEN = os.getenv("SHEET_TOKEN")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text =

 input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

response = requests.post(exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()

today = datetime.now().strftime("%Y-%m-%d")
sheet_inputs = {
    "workout": {
        "date": today,
        "exercise": result["exercises"][0]["name"].title(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"]
    }
}

bearer_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}

sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
print(sheet_response.text)
```


