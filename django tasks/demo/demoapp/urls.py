from django.urls import path
from . import views
from demoapp.views import Home, Adddata

urlpatterns = [
    path('', Home.as_view()),
    path('adddata', Adddata.as_view()),
]