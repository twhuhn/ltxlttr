from django.urls import path
from .views import home, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('form/', contact_view, name='contact'),
]