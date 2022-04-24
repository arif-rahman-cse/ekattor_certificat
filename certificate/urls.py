from django.urls import path

from certificate import views

urlpatterns = [
    path('character-certificate/<int:pk>', views.character_certificate, name='character-certificate'),
]

