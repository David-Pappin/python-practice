import requests

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

def main():

    location = user_location()
    coordinates = location_coordinates(location)
    if coordinates is None:
        print("Weather data was not acquired")
    else: 
        print(coordinates)

if __name__ == "__main__":
    main()
    

