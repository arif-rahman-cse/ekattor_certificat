from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from GeoCodeBD.models import District, Upazila
from user_entry.forms import UserEntryCreateForm, UserEntryUpdateForm
from user_entry.models import UserEntry


@login_required
def add_new_user_data(request):
    template_name = 'user_entry/add_new_user_data.html'

    if request.method == 'GET':
        print("GET called")
        user_data_form = UserEntryCreateForm(None)

    elif request.method == 'POST':
        user_data_form = UserEntryCreateForm(request.POST)
        if user_data_form.is_valid():
            user_data = user_data_form.save(commit=False)
            user_data.created_by = request.user
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


class UserDataListView(LoginRequiredMixin, ListView, ):
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


class UserDataUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserEntry
    form_class = UserEntryUpdateForm
    success_url = reverse_lazy('user-data-list')
    template_name = 'user_entry/edit_user_data.html'
    success_message = "User Data Updated Successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Product Information"
        context["nav_bar"] = "product_list"
        return context


@login_required
def user_profile_preview(request, pk):
    template_name = 'user_entry/user_profile_page.html'

    return render(request, template_name, {
        'user_data': UserEntry.objects.get(pk=pk),
        'title': 'User Profile Preview',
        'nav_bar': 'user_profile_preview'
    })
