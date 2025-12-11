from django.contrib import admin
from django.urls import path
from .views import home, contato, quem_somos, login, signup

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('quem_somos/', quem_somos, name='quem_somos'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
]
