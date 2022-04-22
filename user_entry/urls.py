from django.urls import path

from user_entry import views

urlpatterns = [
    path('new-user-data', views.add_new_user_data, name='add-new-user-data'),
    path('user-data-list', views.UserDataListView.as_view(), name='user-data-list'),
    path('user-data-edit/<int:pk>', views.UserDataUpdateView.as_view(), name='user-data-edit'),
    path('user-profile/<int:pk>', views.user_profile_preview, name='user-profile'),
]

