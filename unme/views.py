from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .forms import LoginForm

#HttpResponse Test View
def test_view(request):
    return HttpResponse("Welcome to UnmE App Test View")


# Login Functionality
def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form':form}) 