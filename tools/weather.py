from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """
    Get current weather for a city.
    """

    weather_data = {
        "Pune": "28°C, Sunny",
        "Mumbai": "31°C, Humid",
        "Delhi": "36°C, Hot"
    }

    return weather_data.get(
        city,
        f"No weather data found for {city}"
    )