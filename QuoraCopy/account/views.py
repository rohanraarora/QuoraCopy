from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import *
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
import base64
import json
from django.db.models import Q
# Create your views here.
@require_GET
def home(request):
    signupForm = SignUpForm();
    loginForm = LoginForm();
    data = {"signupForm":signupForm,"loginForm":loginForm}
    return render(request,"account/index.html",data);

@require_POST
def handleLogin(request):
    if request.user.is_authenticated():
        return redirect('http://www.quora.com')
    f = LoginForm(request.POST)
    nexturl = request.POST.get('next')
    if f.is_valid():
        user = f.get_user();
        login(request, user);
        if not nexturl:
            return redirect('http://www.quora.com')
        else:
            return redirect(nexturl)
    else:
        loginform = f
        signupform = SignupForm()
        data = { 'loginForm' : loginform, 'signupForm' : signupform , 'next' : nexturl }
        return render(request, 'account/index.html', data);

@require_POST
def handleSignup(request):
    if request.user.is_authenticated():
        return redirect('http://www.quora.com')
    f = SignUpForm(request.POST)
    nexturl = request.POST.get('next')
    if f.is_valid():
        user = f.save();
        user.is_active = False;
        user.save();
        url = request.build_absolute_uri(reverse('activate'));
        url = url + "?user=" + base64.b64encode(user.username.encode('utf-8')).decode('utf-8')
        message = ''' welcome to my Awesome instagram. Click <a href= '%s'>here </a> to activate your account ''' % url
        email = EmailMessage('Welcome', message, to=[user.email])
        email.send()
        return redirect('http://www.quora.com')
    else:
        signupform = f
        loginform = LoginForm()
        data = { 'loginForm' : loginform, 'signupForm' : signupform , 'next' : nexturl }
        return render(request, 'account/index.html', data);

@require_GET
def activateaccount(request):
    if request.user.is_authenticated():
        return redirect('http://www.quora.com')
    username = base64.b64decode(request.GET.get('user').encode('utf-8')).decode('utf-8')
    user = get_object_or_404(MyUser, username = username);
    user.is_active = True
    user.save()
    return redirect('http://www.quora.com')
