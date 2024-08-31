from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_recommendations, generate_data_visualisation_context
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


@csrf_exempt
@require_http_methods(["GET", "POST"])
def api_get_recommendations(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        recommendations = get_recommendations(data)
        return JsonResponse(recommendations, safe=False)
    elif request.method == 'GET':
        # Example response for GET request (you can customize this)
        return JsonResponse({"message": "GET request received. Please use POST to get recommendations."})
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def api_data_visualization(request):
    if request.method == 'POST':
        recommendations = json.loads(request.body)
        context = generate_data_visualisation_context(recommendations)
        return JsonResponse(context, safe=False)
    elif request.method == 'GET':
        # Example response for GET request (you can customize this)
        return JsonResponse({"message": "GET request received. Please use POST to get data visualization."})
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
@require_http_methods(["POST"])
def api_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists.'}, status=400)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already in use.'}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({'message': 'User registered successfully.'}, status=201)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
@require_http_methods(["POST"])
def api_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful.'})
        else:
            return JsonResponse({'error': 'Invalid credentials.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)