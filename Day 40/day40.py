import requests
import smtplib
import os

TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_password"

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

def send_email(subject, message):
    with smtplib.SMTP("smtp.example.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:{subject}

{message}"
        )

flight_data = check_flights("New York", "Paris", "01/06/2024", "30/06/2024")
for flight in flight_data:
    email_subject = f"Low price alert! Only ${flight['price']} to fly from {flight['cityFrom']}-{flight['flyFrom']} to {flight['cityTo']}-{flight['flyTo']}, from {flight['route'][0]['local_departure'].split('T')[0]} to {flight['route'][1]['local_departure'].split('T')[0]}."
    email_message = f"Flight details:

{flight['route']}"
    send_email(email_subject, email_message)
