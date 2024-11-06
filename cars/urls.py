from django.urls import path
from . import views # Import your views module
from .views import car_detail

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>',view=car_detail,name='car_detail'),
    path('search', views.search, name='search'),
]
