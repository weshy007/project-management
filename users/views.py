from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from projects.models import Project

from .forms import ProfileForm
from .models import Profile


# Create your views here.
def home(request):
  return render(request, 'index.html')


def projects(request):
    projects = Project.objects.all()
    
    return render(request, 'projects.html', {'projects': projects})


def registration(request):
    if request.method == 'POST':
        form - UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        
    form = UserCreationForm
    return render(request, 'registration.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'login.hmtl'
    form = AuthenticationForm


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def update_profile(request):
    if request.metod == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            form = ProfileForm(instance=request.user.profile)

        return render(request, 'profile-update-form.html', {'form': form})
    
