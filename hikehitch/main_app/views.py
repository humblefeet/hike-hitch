from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Trail, Hiker, Trip
from django.views.generic.edit import CreateView


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def trails_index(request):
    trails = Trail.objects.all()
    return render(request, 'trails/index.html', {'trails':  trails})

def trails_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    return render(request, 'trails/<int:trail_id>', {'trail': trail})

def hikers_index(request):
    hikers = Hiker.objects.all()
    return render(request, 'hikers/index.html', {'hikers': hikers})

def trips(request):
    trips = Trip.objects.all()
    return render(request, 'trips/index.html', {'trips': trips})

def trips_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'trips/<int:trip_id>', {'trip': trip})


@login_required
def profile(request, username):
    if username == request.user.username:
        user = User.objects.get(username=username)
        # hiker = Hiker.objects.get(user=user)
        hiker = user.hiker
        return render(request, 'profile.html', {'username': username, 'hiker': hiker})
    else:
        return HttpResponseRedirect('/')


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
            return HttpResponseRedirect('hikers/create/')
        else:
            form = UserCreationForm()
            errMsg = "One or more fields was invalid, please try again"
            return render(request, 'signup.html', {'form': form, 'err': errMsg})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})



class TrailCreate(CreateView):
    model = Trail
    fields = '__all__'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/trails/')

class HikerCreate(CreateView):
    model = Hiker
    fields = ['first_name','sex', 'age', 'experience','email']
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/trails/')

class TripCreate(CreateView):
    model = Trip
    fields = '__all__'
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponse('/trips/')