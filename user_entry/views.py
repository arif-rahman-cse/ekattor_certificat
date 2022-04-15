from django.shortcuts import render


# Create your views here.
def add_new_user_data(request):
    return render(request, 'user_entry/add_new_user_data.html', {'title': 'Add New User'})
