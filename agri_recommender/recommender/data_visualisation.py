from django.shortcuts import render
import json

def data_visualization_view(request):
    # Example response from the API
    response_data = {
        "fertilizer_recommendations": {
            "chemical": [
                {"type": "NPK 10-26-26", "quantity": "250 kg/hectare", "application_time": "At planting"},
                {"type": "Urea", "quantity": "100 kg/hectare", "application_time": "Split application: 50 kg at 30 days, 50 kg at 60 days after planting"}
            ],
            "organic": [
                {"type": "Vermicompost", "quantity": "5 tons/hectare", "application_time": "2 weeks before planting"},
                {"type": "Neem cake", "quantity": "500 kg/hectare", "application_time": "At planting"}
            ]
        },
        "crop_confirmation": "Tomato (as requested)",
        "alternative_crops": ["Okra", "Chili", "Brinjal"],
        "best_practices": ["Use mulching", "Implement drip irrigation", "Practice crop rotation", "Use integrated pest management", "Consider biofertilizers"],
        "schedule": {
            "sowing_time": "Mid-July",
            "expected_harvest_time": "October-November",
            "key_activities": [
                {"activity": "Transplanting seedlings", "time": "30 days after sowing"},
                {"activity": "First pruning", "time": "45 days after transplanting"},
                {"activity": "Monitoring for diseases", "time": "Throughout the growing season"}
            ]
        },
        "expected_income_impact": "+15%",
        "soil_information": {
            "type": "Red lateritic soil",
            "ph": 6.5,
            "nitrogen": "Medium (280 kg/ha)",
            "phosphorus": "High (25 kg/ha)",
            "potassium": "Medium (190 kg/ha)",
            "organic_matter": "Low (0.5%)",
            "moisture": "65%"
        },
        "nearest_cold_storage": {
            "name": "Pune Agro Cold Storage",
            "distance": "15 km",
            "capacity": "1000 metric tons",
            "type": "Multi-commodity"
        }
    }

    context = {
        'response_data': json.dumps(response_data)
    }

    return render(request, 'data_visualization.html', context)
