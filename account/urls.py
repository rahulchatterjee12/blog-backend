from django.contrib import admin
from django.urls import path

from account.views import RegisterView


urlpatterns = [
    path('register/',RegisterView.as_view())
]
