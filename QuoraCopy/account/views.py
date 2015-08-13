from django.shortcuts import render
from .forms import *

# Create your views here.

def home(request):
    signupForm = SignUpForm();
    loginForm = LoginForm();
    data = {"signupForm":signupForm,"loginForm":loginForm}
    return render(request,"account/index.html",data);
