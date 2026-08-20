import requests
import pprint
import sys
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast"}

base_url = "https://geocoding-api.open-meteo.com/v1/search?name="
def user_location():
    
    while True:
        location = input("Enter location: ")
        if location.strip() == "":
            print("Enter a valid location ")
        else: 
            break
    return location.strip().lower() 

def location_coordinates(location):
    url = f"{base_url}{location}&count=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        latitude = data['results'][0]['latitude']
        longitude = data['results'][0]['longitude']

        coordinates = {"latitude" : latitude,
                       "longitude" : longitude}
        
        return coordinates   
         
    else:
        return None


def weather_data(coordinates):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={coordinates['latitude']}&longitude={coordinates['longitude']}&current_weather=true"
    response = requests.get(url)

    if response.status_code == 200:
        weatherdata = response.json()
        return weatherdata
    else:
        return None

def weather_info(weatherdata):
    w = weatherdata["current_weather"]
    temp = w["temperature"]
    time = w["time"]
    weather_code = w["weathercode"]

    weather_code = WEATHER_CODES.get(weather_code, "Unknown")

    weatherinfo = {"temperature" : temp,
                   "time" : time,
                   "weathercode" : weather_code}

    return weatherinfo
    

def main():

    location = user_location()
    coordinates = location_coordinates(location)
    if coordinates is None:
        print("coordinates were not acquired")
        sys.exit()

    weatherdata = weather_data(coordinates)
    if weatherdata is None:
        print("Weather data was not acquired")
    else:
        weatherinfo = weather_info(weatherdata)
        for k,v in weatherinfo.items():
            print(f"{k} : {v}")
        

if __name__ == "__main__":
    main()
    

