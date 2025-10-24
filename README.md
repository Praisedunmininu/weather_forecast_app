             Weather Forecast Project 
This project is built using the 5-day / 3-hour forecast API from OpenWeatherMap. The API provides weather data every 3 hours for the next 5 days.
My project focuses on showing the temperature, humidity, and weather condition (like cloudy or sunny) for any city of your choice.it currently display the first 5 forecast, which means the weather for the next few hours, not all 5 days yet.
I plan to improve it later so it can show one forecast per day to make it a full 5-day forecast app.How it works

Importing the libraries
I imported three main libraries:

requests – to send a request to the weather API.
dotenv – to load my API key from the .env file safely.
os – to get the environment variable (the API key).

Loading the API key
The .env file stores my API key.

load_dotenv()
api_key = os.getenv("API_KEY")
print("loaded API_KEY:", api_key)
This makes sure my API key is not written directly in the code, which is more secure.

Choosing a city

city = "London"
print(city)
I picked London as an example city, but you can change it to any city you want.

Setting up the API URL and parameters

url = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}
q is the city name
appid is my API key
units tells the API to show temperature in Celsius

Getting data from the API

response = requests.get(url, params=params)
data = response.json()
This part sends the request and gets the weather data in JSON format (like a big dictionary).

Reading and displaying the forecast

forecast_time = data["list"]
for forecast_time in data["list"][:5]:
    time = forecast_time["dt_txt"]
    temp = forecast_time["main"]["temp"]
    description = forecast_time["weather"][0]["description"]
    print(f"Time:{time}, Temp:{temp}°C, Description:{description}")


The API gives several weather forecasts in the "list".
I selected the first 5 forecasts to make it simple.
For each forecast, I printed the time, temperature, and weather condition.

What the program does
When you run the program, it prints something like this:

Time: 2025-10-24 09:00:00, Temp: 18°C, Description: clear sky
Time: 2025-10-24 12:00:00, Temp: 20°C, Description: few clouds
it tells you the temperature and weather for the next five hours in the city you selected .


How to Run This Project

Make sure Python is installed

Install the required packages

Run this command to install the needed libraries:
pip install requests python-dotenv


Get your OpenWeather API key

Go to https://openweathermap.org/api
 and sign up for a free account.

After signing up, copy your API key.

Create a .env file

In your project folder, create a file named .env.
Inside the file, add this line:
API_KEY=your_api_key_here
Replace your_api_key_here with your actual key.

Run the Python file

Open your Python editor (like VS Code or IDLE).
Run the script.
The program will print the weather forecast for your chosen city.

Change the city name if you want

In the code, find this line:
city = "London"
You can change "London" to any city name you want, for example "New york" or "Lagos"
    
    Future Improvements

There are a few things I would like to add or improve in this project later:
Show the full 5-day forecast — I plan to make it display one forecast per day instead of only the first few hours.
Add user input — so users can type in the city name instead of changing it in the code.
Create a simple user interface (UI) — maybe with  Streamlit, so the weather can appear nicely on screen instead of just in the terminal.
Handle errors better — for example, showing a message if the city name is typed wrong or if there is no internet connection.

This tells you the temperature and weather for the next few hours in the city you selected.
