import os
import google.generativeai as genai
from dotenv import load_dotenv
import requests

load_dotenv()

# Setup Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Weather Function
def get_weather(location):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast = data['forecast']['forecastday'][0]['day']
        return f"🌤️ Weather in {location}: {forecast['condition']['text']}, Avg Temp: {forecast['avgtemp_c']}°C"
    else:
        return "❌ Weather data not available."

# AI Chat Function
def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

# Itinerary Function
def suggest_itinerary(destination):
    plans = {
        "Goa": ["Baga Beach", "Dudhsagar Falls", "Candolim Fort"],
        "Manali": ["Solang Valley", "Rohtang Pass", "Old Manali"],
        "Paris": ["Eiffel Tower", "Louvre Museum", "Seine Cruise"]
    }
    return plans.get(destination, ["Explore local landmarks", "Visit museums", "Try local food"])

# Main Travel Planner Flow
def travel_planner():
    print("🌍 Welcome to your AI Travel Planner Agent (Gemini-powered)")
    name = input("👤 Your name: ")
    interests = input("🌄 What kind of places do you like (beaches, mountains, cities)? ")
    budget = input("💰 Your budget (in USD): ")

    # Destination selection (simple logic)
    if "beach" in interests.lower():
        destination = "Goa"
    elif "mountain" in interests.lower():
        destination = "Manali"
    else:
        destination = "Paris"

    print(f"\n✈️ Suggested Destination: {destination}")
    print(get_weather(destination))

    print("\n🗓️ 3-Day Sample Itinerary:")
    for i, activity in enumerate(suggest_itinerary(destination), 1):
        print(f" Day {i}: {activity}")

    print("\n💬 Chat with your AI travel assistant (type 'exit' to stop):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        ai_reply = ask_gemini(f"As a travel assistant, respond to: {user_input}")
        print("🤖 Assistant:", ai_reply)


if __name__ == "__main__":
    travel_planner()
 
