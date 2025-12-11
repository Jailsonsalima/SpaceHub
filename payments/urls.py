from django.contrib import admin
from django.urls import path
from django_pagseguro.views import NotificationView


urlpatterns = [
    path('pagseguro/notification/', NotificationView.as_view(), name='pagseguro_notification'),
]
