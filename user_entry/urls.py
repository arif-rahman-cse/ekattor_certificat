from django.urls import path

from user_entry import views

urlpatterns = [
    path('/new-user-data', views.add_new_user_data, name='add-new-user-data'),
]

