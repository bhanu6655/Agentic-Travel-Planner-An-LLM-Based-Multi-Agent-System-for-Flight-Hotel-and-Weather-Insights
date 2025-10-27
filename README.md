AI Travel & Flight Tracker Agent

An AI-powered multi-agent system that helps users plan their trips intelligently — combining real-time flight tracking, hotel recommendations, weather forecasting, and AI-based conversation using LLMs (Groq, Gemini, etc.).

 Key Features

 AI Agents with Specialized Roles

Flight Agent – Finds and tracks flight details using AI-based reasoning.

Hotel Agent – Recommends top-rated and budget-friendly hotels near your destination.

Weather Agent – Predicts weather conditions for your travel dates using real-time weather APIs.

(Coming Soon) Budget Planner & Transport Route Agent for complete travel assistance.

 Multi-LLM Support

Supports Groq API, Google Gemini API, and WeatherAPI for intelligent, fast, and reliable responses.

Secure Configuration

Uses .env file to safely manage all API keys and credentials.

 Modular Architecture

Each agent is independent and easily replaceable — you can plug in new APIs or AI models without affecting the rest of the system.

<img width="853" height="375" alt="image" src="https://github.com/user-attachments/assets/a62aced6-94ef-4f56-8f37-e14d19a77e13" />


Each module communicates with its respective API or AI model and collaborates through the central travel assistant logic.

🛠️ Tech Stack
Category	Tools / APIs
Programming Language	Python 3.10+
AI Models	Groq API (Llama3 successor), Google Gemini
Weather Data	WeatherAPI.com

Environment Management	python-dotenv
Version Control	Git, GitHub
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/bhanu6655/Flight-Tracker-ai-agent.git
cd Flight-Tracker-ai-agent

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create a .env File

In the project root directory, add your keys:

GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
WEATHER_API_KEY=your_weatherapi_key_here

4️⃣ Run the Application
python ai_agent.py

💬 Example Output
🌦️ Weather Agent:
Expected weather in Paris on 2025-11-03: Partly Cloudy, 23°C, 10% chance of rain.

✈️ Flight Agent:
AI suggests direct flights from Delhi → Paris on 2025-11-03.
Airline: Air France | Price: $720 | Duration: 9h 30m.

 Hotel Agent:
Top 3 hotels near Eiffel Tower:
1. Novotel Paris Tour Eiffel – $180/night
2. Mercure Paris Centre – $210/night
3. Ibis Styles Paris – $150/night

 Future Enhancements

 Route Planning Agent (Google Maps API)

 Budget Optimizer using AI reasoning

 Real-Time Flight Alerts

 Itinerary Generator combining all agent outputs

 Web Interface (React + Flask backend)

 Contributing

Fork the repo 🍴

Create a feature branch

Commit your changes

Push and open a Pull Request

 License

This project is licensed under the MIT License — you’re free to modify and distribute it with attribution.

 Author

G Bhanuprakash
Email: bhanuprakash7984@gmail.com

GitHub: bhanu6655
