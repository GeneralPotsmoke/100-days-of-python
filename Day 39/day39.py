import requests
import os

TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")

def get_destination_code(city_name):
    location_endpoint = "https://tequila-api.kiwi.com/locations/query"
    headers = {"apikey": TEQUILA_API_KEY}
    query = {"term": city_name, "location_types": "city"}
    response = requests.get(location_endpoint, headers=headers, params=query)
    results = response.json()["locations"]
    code = results[0]["code"]
    return code

def check_flights(origin_city, destination_city, from_time, to_time):
    search_endpoint = "https://tequila-api.kiwi.com/v2/search"
    headers = {"apikey": TEQUILA_API_KEY}
    query = {
        "fly_from": get_destination_code(origin_city),
        "fly_to": get_destination_code(destination_city),
        "date_from": from_time,
        "date_to": to_time,
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "max_stopovers": 0,
        "curr": "USD"
    }
    response = requests.get(search_endpoint, headers=headers, params=query)
    data = response.json()["data"]
    return data

flight_data = check_flights("New York", "Paris", "01/06/2024", "30/06/2024")
print(flight_data)
