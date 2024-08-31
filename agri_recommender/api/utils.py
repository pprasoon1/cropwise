import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import json
import logging

# Use your API key
genai.configure(api_key=os.environ.get('GOOGLE_AI_STUDIO_API_KEY', 'AIzaSyAff6A2OeToIyqWhWJecMBkETbDmJxnh94'))

def get_recommendations(data):
    # Configure the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    safety_settings = [
        {
            "category": HarmCategory.HARM_CATEGORY_HARASSMENT,
            "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        },
        {
            "category": HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        },
        {
            "category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        },
        {
            "category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        },
    ]
    model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    prompt_parts = (
        f"Given the following agricultural data:\n"
        f"State: {data['state']}\n"
        f"District: {data['district']}\n"
        f"Block: {data.get('block', 'Not specified')}\n"
        f"Crop: {data.get('crop', 'Not specified')}\n"
        f"Start Month: {data.get('start_month', 'Not specified')}\n\n"
        f"Provide comprehensive agricultural recommendations in the following JSON format:\n"
        f"{{"
        f"\"fertilizer_recommendations\": {{"
        f"\"chemical\": [{{"
        f"\"type\": \"fertilizer name\", "
        f"\"quantity\": \"amount in kg/hectare\", "
        f"\"application_time\": \"when to apply\""
        f"}},...], "
        f"\"organic\": [{{"
        f"\"type\": \"organic fertilizer name\", "
        f"\"quantity\": \"amount in kg/hectare or tons/hectare\", "
        f"\"application_time\": \"when to apply\""
        f"}},...]}}, "
        f"\"crop_recommendations\": [{{"
        f"\"crop\": \"crop name\", "
        f"\"variety\": \"variety name\""
        f"}},...], "
        f"\"best_practices\": [\"practice1\", \"practice2\", ...], "
        f"\"schedule\": {{"
        f"\"sowing_time\": \"recommended sowing time\", "
        f"\"expected_harvest_time\": \"expected harvest time\", "
        f"\"key_activities\": [{{"
        f"\"activity\": \"activity name\", "
        f"\"time\": \"when to perform\""
        f"}},...]}}, "
        f"\"expected_income_impact\": \"percentage increase or decrease\", "
        f"\"soil_information\": {{"
        f"\"type\": \"soil type\", "
        f"\"ph\": pH_value, "
        f"\"nitrogen\": \"amount and level\", "
        f"\"phosphorus\": \"amount and level\", "
        f"\"potassium\": \"amount and level\", "
        f"\"organic_matter\": \"percentage and level\", "
        f"\"moisture\": \"percentage of field capacity\""
        f"}}, "
        f"\"nearest_cold_storage\": {{"
        f"\"name\": \"storage facility name\", "
        f"\"distance\": \"distance in km\", "
        f"\"capacity\": \"storage capacity\", "
        f"\"type\": \"type of storage\""
        f"}}"
        f"}}"
    )

    response = model.generate_content(prompt_parts)
    
    # Extract the JSON part of the response
    response_text = response.text
    # Look for the start and end of the JSON part
    start_index = response_text.find('{')
    end_index = response_text.rfind('}')
    
    if start_index != -1 and end_index != -1:
        json_str = response_text[start_index:end_index+1]
        try:
            recommendations = json.loads(json_str)
            return recommendations
        except json.JSONDecodeError:
            logging.error("Failed to parse AI response: %s", json_str)
            return {}
    else:
        logging.error("Failed to find JSON in AI response: %s", response_text)
        return {}

def get_income_growth_data():
    # Placeholder function - replace with actual data fetching logic
    return {
        'Crop A': 30,
        'Crop B': 40,
        'Crop C': 50,
        'Crop D': 60,
        'Others': 10
    }

def get_weather_forecast():
    # Placeholder function - replace with actual weather API call
    return {
        'Sunny': 60,
        'Cloudy': 20,
        'Rainy': 15,
        'Stormy': 5
    }

def process_soil_information(soil_info):
    if soil_info:
        return {
            'ph': soil_info.get('ph'),
            'nitrogen': soil_info.get('nitrogen'),
            'phosphorus': soil_info.get('phosphorus'),
            'potassium': soil_info.get('potassium'),
            'organic_matter': soil_info.get('organic_matter'),
            'moisture': soil_info.get('moisture'),
        }
    return {}

def generate_data_visualisation_context(api_response):
    context = {
        'soil_information': process_soil_information(api_response.get('soil_information')),
        'fertilizer_recommendations': api_response.get('fertilizer_recommendations'),
        'expected_income_impact': api_response.get('expected_income_impact'),
        'nearest_cold_storage': api_response.get('nearest_cold_storage'),
        # Add other required data from the API response
    }
    return context

