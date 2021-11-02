from django.contrib import admin
from django.urls import path
from .views import MutantsappViewSet

urlpatterns = [
    path('', MutantsappViewSet.as_view())
]