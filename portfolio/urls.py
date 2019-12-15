from django.urls import path
from .views import HomeView


app_name = 'portfolio'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]