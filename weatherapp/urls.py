from django.urls import path
from . import views

urlpatterns = [
        path('',views.weatherhome, name= 'weathersimple'),
        path('/weatherloop',views.weatherloop, name = 'weatherloop'),
]
