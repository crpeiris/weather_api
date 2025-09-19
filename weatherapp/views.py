import requests
from django.shortcuts import render
from .forms import CityForm
from django.conf import settings

# Create your views here.
def weatherhome(request):
    api_key = "9bf50f1140004b98835191651251209"
    weather_data = {}
    error_msg = ""

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            url = "http://api.weatherapi.com/v1/current.json"
            params = {"q": city, "key": api_key}
            response = requests.get(url, params=params).json()

            if "error" not in response:
                weather_data = {
                    "city_entered": city,
                    "city": response["location"]["name"],
                    "temperature": response["current"]["temp_c"],
                    "text": response["current"]["condition"]["text"],
                    "icon": response["current"]["condition"]["icon"],
                    "country": response["location"]["country"],
                    "lat": response["location"]["lat"],
                    "lon": response["location"]["lon"],
                }
            else:
                error_msg = response["error"]["message"]
    else:
        form = CityForm()

    return render(
        request,
        "weatherapp/weatherhome.html",
        {
            "form": form,
            "weather_data": weather_data,
            "error_msg": error_msg,
            "google_maps_key": settings.GOOGLE_MAPS_API_KEY,
        },
    )

# A view to pass the Json object as it is to the template.
def weatherloop(request):
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
    return render(request, 'weatherapp/weatherloop.html', {'form': form,'res_object' : response })


# A view to pass the Json object as it is to the template.
def htmlform(request):
    api_key = '9bf50f1140004b98835191651251209'

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if city:
            url = f'http://api.weatherapi.com/v1/current.json?q={city}&key={api_key}'
            response = requests.get(url).json()
        # else: leave response empty for invalid input
        else:
            weather_data = {}
    else:
        form = CityForm()
        response = {}
    return render(request, 'weatherapp/htmlform.html', {'res_object' : response })
