from django.urls import path
from . import views

urlpatterns = [
        path('',views.weatherhome),
        path('/simpleloop',views.simpleloop, name = 'simpleloop'),
]
