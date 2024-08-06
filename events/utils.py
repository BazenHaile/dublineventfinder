# This file contains utility functions used across the application

import requests
from django.conf import settings

def geocode_location(location):
    """
    This function takes a location name and returns its latitude and longitude.
    It uses the OpenCage Geocoding API to convert addresses into geographic coordinates.
    """
    
    # Get the API key from the project settings
    api_key = settings.OPENCAGE_API_KEY
    
    # The base URL for the OpenCage Geocoding API
    base_url = "https://api.opencagedata.com/geocode/v1/json"
    
    # Parameters for the API request
    params = {
        'q': location,  # The location we want to geocode
        'key': api_key,  # Our API key
        'limit': 1,  # We only want the top result
    }
    
    # Send a GET request to the API
    response = requests.get(base_url, params=params)
    
    # Parse the JSON response
    results = response.json()
    
    # Check if we got any results
    if results and results['results']:
        # Extract the latitude and longitude from the first result
        location = results['results'][0]['geometry']
        return location['lat'], location['lng']
    
    # If no results were found, return None for both latitude and longitude
    return None, None