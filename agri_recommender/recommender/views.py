from django.shortcuts import render, redirect
from .forms import AgriForm
from .utils import get_recommendations, get_income_growth_data, get_weather_forecast, generate_data_visualisation_context, get_recommendations
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def landing(request):
    return render(request, 'landing.html')
@csrf_exempt
def home(request):
    if request.method == 'POST':
        form = AgriForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recommendations = get_recommendations(data)
            request.session['recommendations'] = json.dumps(recommendations)
            return redirect('results')
    else:
        form = AgriForm()
    return render(request, 'form.html', {'form': form})

@csrf_exempt
def results(request):
    recommendations = json.loads(request.session.get('recommendations', '{}'))
    return render(request, 'results.html', {'recommendations': recommendations})
@csrf_exempt
def data_visualization(request):
    # Sample data
    soil_information = {
        'ph': 6.5,
        'nitrogen': '15 mg/kg',
        'phosphorus': '20 mg/kg',
        'potassium': '25 mg/kg',
        'organic_matter': '3.5%',
        'moisture': '10%'
    }

    # Extract numeric values
    def extract_numeric(value):
        # Extract numeric value from strings like '15 mg/kg'
        return float(''.join(filter(str.isdigit, value)))

    processed_data = {
        'ph': soil_information['ph'],
        'nitrogen': extract_numeric(soil_information['nitrogen']),
        'phosphorus': extract_numeric(soil_information['phosphorus']),
        'potassium': extract_numeric(soil_information['potassium']),
        'organic_matter': extract_numeric(soil_information['organic_matter'].replace('%', '')),
        'moisture': extract_numeric(soil_information['moisture'].replace('%', ''))
    }

    return render(request, 'data_visualization.html', {'soil_information': processed_data})