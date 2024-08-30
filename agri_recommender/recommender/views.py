from django.shortcuts import render, redirect
from .forms import AgriForm, RegisterForm, LoginForm
from .utils import get_recommendations, get_income_growth_data, get_weather_forecast, generate_data_visualisation_context, get_recommendations
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


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




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})
def latest_articles(request):
    articles = [
        {"title": "New Farming Techniques to Increase Yield", "summary": "Learn about the latest farming techniques to boost your crop yield.", "date": "2024-08-30"},
        {"title": "Government Schemes for Farmers in 2024", "summary": "Explore the latest government schemes that benefit farmers.", "date": "2024-08-29"},
        {"title": "Weather Update: Preparing for the Upcoming Season", "summary": "Get the latest weather updates and how to prepare for the upcoming farming season.", "date": "2024-08-28"},
    ]
    return render(request, 'latest_articles.html', {'articles': articles})