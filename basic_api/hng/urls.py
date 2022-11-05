from django.urls import path
from .views import get_user_details, calculate


urlpatterns = [
    path('user-information/', get_user_details, name='get_user_details'),
    path('calculate/', calculate, name='calculate'),
]
