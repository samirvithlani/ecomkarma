from django.shortcuts import render
from django.views.generic import ListView,DetailView,FormView
from django.contrib.auth.hashers import make_password

from .forms import UserForm
# Create your views here.

class UserRegisterView(FormView):
    form_class = UserForm
    template_name = 'user/register.html'
    success_url ="/"
    
    def form_valid(self, form):
        user = form.save()
        #password hasing
        user.is_staff = True
        user.password = make_password(form.cleaned_data['password'])
        user.save()    
        return super().form_valid(form)
    