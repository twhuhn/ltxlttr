from django.urls import path
from .views import home, clear

urlpatterns = [
    path('', home, name='home'),
    path('clear', clear, name='clear')
]