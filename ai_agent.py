import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# API URLs
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Common headers
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# --------------------------- FLIGHT AGENT --------------------------- #

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
        return f"✈️ Flight Agent Error: {response.status_code} - {response.text}"

# --------------------------- HOTEL AGENT --------------------------- #

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
        return f"🏨 Hotel Agent Error: {response.status_code} - {response.text}"

# --------------------------- WEATHER AGENT --------------------------- #

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
🌦️ **Weather Forecast for {city} ({date}):**
- Condition: {day_data['condition']['text']}
- Avg Temp: {day_data['avgtemp_c']}°C
- Max Temp: {day_data['maxtemp_c']}°C
- Min Temp: {day_data['mintemp_c']}°C
- Rain Chance: {day_data['daily_chance_of_rain']}%
"""
            else:
                return f"⚠️ Forecast data not available for {date}. (Free tier supports only 3-day forecasts.)"
        else:
            current = data["current"]
            return f"""
🌤️ **Current Weather in {city}:**
- Condition: {current['condition']['text']}
- Temperature: {current['temp_c']}°C
- Feels Like: {current['feelslike_c']}°C
- Humidity: {current['humidity']}%
- Wind: {current['wind_kph']} km/h
"""
    else:
        return f"🌧️ Weather Agent Error: {response.status_code} - {response.text}"

# --------------------------- ITINERARY GENERATOR AGENT --------------------------- #

itinerary_instructions = """
You are an AI itinerary planner that creates structured, day-wise travel itineraries.
You will receive:
- Flight details
- Hotel details
- Weather info
- Destination and travel dates

Use these to design a short, realistic travel plan (2–5 days) including:
- Activities & sightseeing suggestions
- Meal or cultural recommendations
- Weather-based adjustments (e.g., indoor plans if rainy)
Keep it structured, concise, and practical.
"""

def generate_itinerary(destination, start_date, duration_days, flight_info, hotel_info, weather_info):
    user_context = f"""
Destination: {destination}
Travel Dates: Starting {start_date} for {duration_days} days
Flight Info: {flight_info}
Hotel Info: {hotel_info}
Weather Info: {weather_info}
"""
    body = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": itinerary_instructions},
            {"role": "user", "content": user_context}
        ],
        "temperature": 0.8
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"🧳 Itinerary Agent Error: {response.status_code} - {response.text}"

# --------------------------- MASTER TRAVEL ASSISTANT --------------------------- #

def travel_assistant(user_query):
    """Route queries to the correct agent."""
    if any(word in user_query.lower() for word in ["flight", "airline", "ticket"]):
        return "✈️ Flight Agent:\n" + ask_flight_agent(user_query)
    elif any(word in user_query.lower() for word in ["hotel", "stay", "room"]):
        return "🏨 Hotel Agent:\n" + ask_hotel_agent(user_query)
    elif any(word in user_query.lower() for word in ["weather", "forecast"]):
        return "🌦️ Weather Agent:\n" + ask_weather_agent(user_query)
    else:
        return "🤖 Please specify whether you want flight, hotel, or weather details."

# --------------------------- MAIN EXECUTION --------------------------- #

if __name__ == "__main__":
    # Example queries
    query1 = "Find me a flight from Hyderabad to Delhi on 15th April 2025 under $100."
    flight_info = ask_flight_agent(query1)
    print(f"✈️ Flight Agent:\n{flight_info}\n")

    query2 = "Find me 3 affordable hotels in Delhi near Connaught Place for 2 nights in April 2025."
    hotel_info = ask_hotel_agent(query2)
    print(f"🏨 Hotel Agent:\n{hotel_info}\n")

    city = "Delhi"
    date = "2025-04-15"
    weather_info = ask_weather_agent(city, date)
    print(f"🌦️ Weather Agent:\n{weather_info}\n")

    # Generate full itinerary
    itinerary = generate_itinerary(destination="Delhi", start_date="2025-04-15", duration_days=4,
                                   flight_info=flight_info, hotel_info=hotel_info, weather_info=weather_info)
    print(f"🧳 Itinerary Generator:\n{itinerary}")
