from django.urls import path
from .views import homeKasView


urlpatterns = [
    path('', homeKasView.as_view(), name='home')
]
