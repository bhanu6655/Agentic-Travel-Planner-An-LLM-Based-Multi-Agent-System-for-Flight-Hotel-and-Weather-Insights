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
1️ Clone the Repository
git clone https://github.com/bhanu6655/Flight-Tracker-ai-agent.git
cd Flight-Tracker-ai-agent

2️ Install Dependencies
pip install -r requirements.txt

3️ Create a .env File

In the project root directory, add your keys:

GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
WEATHER_API_KEY=your_weatherapi_key_here

4️ Run the Application
python ai_agent.py

 Example Output
 <img width="867" height="538" alt="flight Details" src="https://github.com/user-attachments/assets/db4a1046-3df4-4486-88c1-55b2dd15e14e" />

<img width="1117" height="755" alt="Hotel and Weather Details" src="https://github.com/user-attachments/assets/81e5abb0-e62c-4007-b252-a75f44a96b98" />


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
