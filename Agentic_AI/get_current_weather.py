from langchain_core.tools import tool
from typing import Annotated

@tool
def get_current_weather(city_name: Annotated[str, "it will get a city name"]):
    '''
    this tool will return the current weather or temperature for the given city

    Parameters:
    city_name (str): it is a city name.

    Returns:
    str: The weather of the given city.
    '''
    
    text = f"the weather at city {city_name} is currently sunny"
    return text