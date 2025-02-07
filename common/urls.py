from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.get_countries),
    path('provinces/', views.get_provinces),
    path('cities/', views.get_cities),
    path('modules/', views.get_modules),
    path('privileges/', views.get_privileges),
]
