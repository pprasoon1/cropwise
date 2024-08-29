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
        f"Block: {data['block']}\n"
        f"Crop: {data.get('crop', 'Not specified')}\n"
        f"Start Month: {data.get('start_month', 'Not specified')}\n\n"
        f"Provide agricultural recommendations in the following JSON format:\n"
        f"{{\"fertilizer_recommendations\": [{{"
        f"\"type\": \"fertilizer name\", "
        f"\"quantity\": \"amount in kg/hectare\"}},"
        f"...], "
        f"\"crop_recommendations\": [\"crop1\", \"crop2\", ...], "
        f"\"best_practices\": [\"practice1\", \"practice2\", ...]}}"
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