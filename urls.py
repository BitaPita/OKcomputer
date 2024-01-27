from django.urls import path
from . import views

app_name = 'house'
urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('edithouse/<int:pk>/',views.edithouse, name='edithouse'),
    path('add/',views.house_create, name='add'),
    path('deletehouse/<int:pk>/', views.deletehouse, name='deletehouse')
]