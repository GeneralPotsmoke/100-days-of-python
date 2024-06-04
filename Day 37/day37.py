import requests
import os

USERNAME = "your_username"
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create a new user
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# Create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}
headers = {"X-USER-TOKEN": TOKEN}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# Add a pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": "20230601",
    "quantity": "2",
}
response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)
