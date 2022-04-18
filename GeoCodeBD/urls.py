from django.urls import path

from GeoCodeBD import views

urlpatterns = [
    path('get-all-division', views.get_all_division, name='get-all-division'),
]

