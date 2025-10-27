
import os
import requests
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"


headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}


#  FLIGHT AGENT

flight_instructions = """
You are a flight travel expert focused only on flights.
Given a query, provide 3 flight options including:

- Airline
- Stops
- Flight Duration
- Flight Number
- Class
- Estimated Cost (in USD)

Do NOT include hotel or tour details.
Keep answers structured and short.
"""

def ask_flight_agent(user_query):
    body = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": flight_instructions},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"


#  HOTEL AGENT

hotel_instructions = """
You are a hotel booking assistant focused only on hotels.
Given a user query, provide 3 hotel options including:

- Hotel Name
- Star Rating
- Location
- Price per Night (USD)
- Amenities (Wi-Fi, Breakfast, Pool, etc.)
- Booking Platform Suggestion (e.g., Booking.com, Expedia)

Do NOT include flight or transport details.
Keep answers short and structured.
"""

def ask_hotel_agent(user_query):
    body = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": hotel_instructions},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"
    






# Weather Agent
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
def ask_weather_agent(city, date=None):
    base_url = "https://api.weatherapi.com/v1"

    if date:
        endpoint = f"{base_url}/forecast.json"
        params = {"key": WEATHER_API_KEY, "q": city, "dt": date}
    else:
        endpoint = f"{base_url}/current.json"
        params = {"key": WEATHER_API_KEY, "q": city}

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()

        if date:
            if "forecast" in data and data["forecast"]["forecastday"]:
                day_data = data["forecast"]["forecastday"][0]["day"]
                return f"""
 **Weather Forecast for {city} ({date}):**
- Condition: {day_data['condition']['text']}
- Avg Temp: {day_data['avgtemp_c']}°C
- Max Temp: {day_data['maxtemp_c']}°C
- Min Temp: {day_data['mintemp_c']}°C
- Rain Chance: {day_data['daily_chance_of_rain']}%
"""
            else:
                return f" Forecast data not available for {date}. (Free tier only supports 3-day forecasts.)"
        else:
           
            current = data["current"]
            return f"""
 **Current Weather in {city}:**
- Condition: {current['condition']['text']}
- Temperature: {current['temp_c']}°C
- Feels Like: {current['feelslike_c']}°C
- Humidity: {current['humidity']}%
- Wind: {current['wind_kph']} km/h
"""
    else:
        return f"Error: {response.status_code} - {response.text}"



def travel_assistant(user_query):
    """Decide whether to use the flight or hotel agent based on the query."""
    if any(word in user_query.lower() for word in ["flight", "airline", "ticket"]):
        return " Flight Agent:\n" + ask_flight_agent(user_query)
    elif any(word in user_query.lower() for word in ["hotel", "stay", "room"]):
        return " Hotel Agent:\n" + ask_hotel_agent(user_query)
    else:
        return " Please specify whether you want flight or hotel information."



if __name__ == "__main__":

    query1 = "Find me a flight from Hyderabad to Delhi on 15th April 2025 under $100."
    print(travel_assistant(query1))


    query2 = "Find me 3 affordable hotels in Delhi near Times Square for 2 nights in April 2025."
    print("\n" + travel_assistant(query2))

    city = "Delhi"
    date = "2025-10-29"  
    print("\n Weather Agent:\n")
    print(ask_weather_agent(city, date))



