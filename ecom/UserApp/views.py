from django.shortcuts import render
from django.views.generic import ListView,DetailView,FormView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView,LogoutView    
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail



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
        email = form.cleaned_data['email']
        subject = 'welcome'
        message = 'Welcome to karma Ecom'
        email_from = settings.EMAIL_HOST_USER
        recipen_list = [email]
        send_mail(subject,message,email_from,recipen_list)
        user.password = make_password(form.cleaned_data['password'])
        user.save()    
        return super().form_valid(form)
    
    
class UserLogin(LoginView):
    template_name = "user/login.html"
    
class UserLogoutView(LogoutView):
    reverse_lazy('user:userlogin')