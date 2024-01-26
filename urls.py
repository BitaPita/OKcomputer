from django.contrib import admin
from django.urls import path, include
from .views import login, signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('houses.url')),
    path('users/', 'users.url'),

    path('', login),
    path('', signup)
]