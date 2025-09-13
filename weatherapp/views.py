import requests
from django.shortcuts import render
from .forms import CityForm

# Create your views here.
def weatherhome(request):
    api_key = '9bf50f1140004b98835191651251209'
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            url = 'http://api.weatherapi.com/v1/current.json?q='+ city + '&key=' + api_key
            response = requests.get(url.format(city)).json()
            weather_data = {
                'city_entered': city,
                'temperature': response['current']['temp_c'],
                'city': response['location']['name'],
                'country': response['location']['country'],
            }
        else:
            weather_data = {}
    else:
        form = CityForm()
        weather_data = {}
    return render(request, 'weatherapp/weatherhome.html', {'form': form, 'weather_data': weather_data })


import requests
from django.shortcuts import render
from .forms import CityForm

# A view to pass the Json object as it is to the template.
def simpleloop(request):
    api_key = '9bf50f1140004b98835191651251209'
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            url = 'http://api.weatherapi.com/v1/current.json?q='+ city + '&key=' + api_key
            response = requests.get(url.format(city)).json()
        else:
            weather_data = {}
    else:
        form = CityForm()
        response = {}
    return render(request, 'weatherapp/simpleloop.html', {'form': form,'res_object' : response })
