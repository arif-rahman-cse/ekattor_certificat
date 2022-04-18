from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.views.generic import ListView

from user_entry.forms import UserEntryCreateForm
from user_entry.models import UserEntry


def add_new_user_data(request):
    template_name = 'user_entry/add_new_user_data.html'

    if request.method == 'GET':
        print("GET called")
        user_data_form = UserEntryCreateForm(None)

    elif request.method == 'POST':
        print("Post called")
        user_data_form = UserEntryCreateForm(request.POST)
        if user_data_form.is_valid():
            user_data = user_data_form.save(commit=False)
            print('id: ', request.user.id)
            user_data.created_by = User.objects.get(id=request.user.id)
            user_data.status = True
            user_data.save()

            messages.add_message(request, messages.SUCCESS, 'New Sales Entry Successful')
            return redirect('user-data-list')

        else:
            print("Not Valid Create Form")
            print(user_data_form.errors)
            print(user_data_form.errors)

    return render(request, template_name, {
        'user_data_form': user_data_form,
        'title': 'Add New User Data',
        'nav_bar': 'add_new_user_data'
    })


class UserDataListView(ListView, ):
    model = UserEntry  # Model I want to Covert to List
    template_name = 'user_entry/user_data_list.html'  # Template Name
    context_object_name = 'user_data'  # Change default name of objectList
    ordering = ['-created_at', '-updated_at']  # Ordering post LIFO
    paginate_by = 20  # number of page I want to show in single page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User Data List"
        context["nav_bar"] = "user_data_list"
        context['user_data'] = self.model.objects.all()
        return context
