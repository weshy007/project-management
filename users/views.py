from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import ProfileForm
from .models import Profile

# Create your views here.
def projects(request):
    pass