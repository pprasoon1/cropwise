from django.shortcuts import render, redirect
from .forms import AgriForm
from .utils import get_recommendations, get_income_growth_data, get_weather_forecast
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
    income_growth_data = get_income_growth_data()
    weather_forecast = get_weather_forecast()
    return render(request, 'data_visualization.html',
                   {'income_growth_data': income_growth_data, 
                    'weather_forecast': weather_forecast
                    })
