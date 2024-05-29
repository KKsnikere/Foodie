from django.shortcuts import render
from .models import Food
from django.utils import timezone
import requests


# Create your views here.
def home(request):
    import json
    import requests

    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'KPRDW962v3cUCEqyw6dUxQ==OqepUoiUTffJW9fJ'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
            Food.objects.create(name=api[0]['name'], calories=api[0]['calories'])
        except Exception as e:
            api = "There was an error"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})


def food_search(request):
    if request.method == 'POST':
        food_name = request.POST.get('query')

        # URL и ключ API
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_key = 'KPRDW962v3cUCEqyw6dUxQ==OqepUoiUTffJW9fJ'

        # Параметры для запроса к API
        params = {
            "food_name": food_name,
            "api_key": api_key
        }

        try:
            # Отправка запроса к API
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # Поднимает исключение при ошибке HTTP

            # Обработка полученных данных
            food_data = response.json()
            calories = food_data['calories']

            # Передача данных в шаблон
            return render(request, 'home.html', {
                'food_name': food_name,
                'calories': calories,
            })

        except requests.exceptions.RequestException as e:
            # Обработка ошибок запроса
            return render(request, 'home.html', {'error': str(e)})



    return render(request, 'home.html')

