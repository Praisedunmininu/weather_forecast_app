import requests
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")
print("loaded API_KEY:",api_key)
city = "london"
print(city)
url= "https://api.openweathermap.org/data/2.5/forecast"
params ={
    "q":city,
    "appid":api_key,
    "units":"metric"
}
response = requests.get(url,params=params)
data =response.json()
print(data)
forecast_time = data["list"]
for forecast_time in data["list"][:5]:
    time = forecast_time["dt_txt"]
    temp = forecast_time["main"]["temp"]
    description = forecast_time["weather"][0]["description"]
    print(f"Time:{time},Temp:{temp}°C, Description:{description}")
    










    





