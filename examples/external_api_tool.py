import requests
from langchain_core.tools import tool

@tool
def get_joke():
    """Get a random joke"""

    response = requests.get(
        "https://official-joke-api.appspot.com/random_joke"
    )

    return response.json()

print(get_joke.invoke({}))