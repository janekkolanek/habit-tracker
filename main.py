import requests
from datetime import datetime

USERNAME = "YOUR PIXELA USERNAME"
TOKEN = "YOUR PIXELA TOKEN"
GRAPH_ID = "YOUR PIXELA GRAPH NAME"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# PART 1 - CREATING USER

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# END OF PART 1

# PART 2 - CREATING GRAPH

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# COMMENT THESE 2 LINES AFTER CREATING A GRAPH
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# END OF PART 2

# PART 3 - ADDING PIXEL

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
print(response.text)

# END OF PART 3

