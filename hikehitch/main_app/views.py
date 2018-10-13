from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Trail


# Create your views here.

def index(request):
    return render(request, 'index.html')

def trails_index(request):
    return render(request, 'trails/index.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def trails_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    return render(request, 'trails/<int:trail_id>', {'trail': trail})


def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/trails/')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/')
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('trails/index.html')
        else:
            form = UserCreationForm()
            errMsg = "One or more fields was invalid, please try again"
            return render(request, 'signup.html', {'form': form, 'err': errMsg})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})