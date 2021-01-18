from django.urls import path
from .views import HomeKasView


urlpatterns = [
    path('', HomeKasView.as_view(), name='home')
]
