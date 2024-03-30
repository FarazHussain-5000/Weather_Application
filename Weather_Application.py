import requests

def Get_Weather(LOCATION, API_KEY="bd475cc7d3c93c1d1a695ad7e1f094dc"):

    URL = f"https://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}"
    Response = requests.get(URL)
    if Response.status_code == 200:
        return Response.json()
    else:
        print(f"Error: {Response.status_code}")
        return None

def Display_Weather(Data):

    if Data:
        City = Data["name"] + ", " + Data["sys"]["country"]
        Temperature = Data["main"]["temp"] - 273.16  # Convert Kelvin to Celsius
        Description = (Data["weather"][0]["description"]).title()
        Feels_Like = Data["main"]["feels_like"] - 273.16  # Convert Kelvin to Celsius
        Humidity = Data["main"]["humidity"]
        Wind = Data["wind"]["speed"]

        print(Data)

        print(f"Weather in {City}:")
        print(f"Temperature: {Temperature:.2f}°C")
        print(f"Description: {Description}")
        print(f"Feels Like: {Feels_Like:.2f}°C")
        print(f"Humidity: {Humidity}")
        print(f"Wind: {Wind}")
    else:
        print("UNABLE TO RETRIEVE WEATHER DATA!")

def main():
    Location = str(input("ENTER CITY NAME OR ZIP CODE: "))

    Weather_Data = Get_Weather(Location)

    Display_Weather(Weather_Data)

if __name__ == "__main__":
    main()