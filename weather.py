import schedule
import time

def get_weather(latitude, longitude):
    base_url = f"https://api.open-weteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    response = request.get(base_url)
    data = response.json()
    return data

def send_weather_update():
    # Hardcoded latitude and longitude for New York City
    latitude = 40.7128
    longitude = -74.0060

    weather_data = get_weather(latitude, longitude)

def main():
    schedual.every().day.at("8:00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)
if  __name_- == "__main__":
    main()