import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CityForm
from .models import City
# Create your views here.
def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3d9bdb11a7bf434a610af4eb33dba7e2"
    err_msg = ''
    message = ''
    message_class = ''
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data["City"]
            existing_city_count = City.objects.filter(City=new_city).count()
            if existing_city_count == 0:
                city_exist = requests.get(url.format(new_city)).json()
                if city_exist['cod'] == 200:
                    form.save()
                    success_message = "City succesfully added"
                else:
                    err_msg = "City doesn't exist in the world"
            else:
                err_msg = "City already in the database"
    
        if err_msg:
            message = err_msg
            message_class = "is-danger"
        else:
            message = success_message
            message_class = "is-success"
    form = CityForm()
    weatherData = []
    cities = City.objects.all()
    for city in cities:
        response = requests.get(url.format(city)).json()
        
        city_weather = {
            "city": city,
            "temperature": response["main"]["temp"],
            "description":response["weather"][0]["description"],
            "icon": response["weather"][0]["icon"]
        }
        weatherData.append(city_weather)
   
    context = {"weatherData":weatherData, "form":form, "message":message, "message_class":message_class}
    return render(request, "weather_app/weather.html", context,)

def deleteCity(request, city_name):
    City.objects.filter(City = city_name).delete()
    return redirect('index')