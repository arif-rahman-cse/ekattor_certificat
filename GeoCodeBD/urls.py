from django.urls import path

from GeoCodeBD import views

urlpatterns = [
    path('get-district-by-division', views.get_district_by_division, name='get-district-by-division'),
    path('get-thana-by-district', views.get_thana_by_district, name='get-thana-by-district'),
    path('get-union-by-thana', views.get_union_by_thana, name='get-union-by-thana'),
]

