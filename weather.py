from twilio.rest import Client
from sched import scheduler
import time
import requests

def get_weather(latitude, longitude):
    # base_url = f"https://api.open-weteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    sub_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,windspeed_10m&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch"
    response = requests.get(sub_url)
    data = response.json()
    # print(data)
    print(response.status_code)
    return data

def send_text_message(body):
    account_sid = "ACc4d75cd31d39abaac21b72d407010e6d"
    auth_token = "2eef84790d698ae7b18100636855c008"
    from_phone_number = "+18555405817"
    to_phone_number = "+18593683048"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=from_phone_number,
        to=to_phone_number
    )
    print("Text message sent!")
    # print(message.sid)

def send_weather_update():
    # Hardcoded latitude and longitude for New York City
    latitude = 40.7128
    longitude = -74.0060
    weather_data = get_weather(latitude, longitude)
    temperature = weather_data["hourly"]["temperature_2m"][0]
    relative_humidity = weather_data["hourly"]["relativehumidity_2m"][0]
    wind_speed = weather_data["hourly"]["windspeed_10m"][0]
    weather_info = (
        f"Good morning sir Logan!\n"
        f"Current weather in Lexington:\n"
        f"Temperuature: {temperature:.2f}°F\n"
        f"Relative Humidity: {relative_humidity}%\n"
        f"Wind Speed: {wind_speed}MPH"
    )
    send_text_message(weather_info)


def main():
    scheduler.every().day.at("8:00").do(send_weather_update)
    # send_weather_update()
    while True:
        scheduler.run_pending()
        time.sleep(1)
if  __name__ == "__main__":
    main()