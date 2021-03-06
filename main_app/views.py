from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Trail, Hiker, Trip
from django.views.generic.edit import CreateView,  UpdateView, DeleteView
from django.utils.decorators import method_decorator

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def wish(request):
    return  render(request, 'wish.html')

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
    trails = trip.trail.all()
    hikers = trip.hiker.all()
    return render(request, 'trips/detail.html', {'trip': trip, 'trails':trails, 'hikers':hikers})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    if not hasattr(user, 'hiker'):
        return HttpResponseRedirect('/signup/hikers/create/')
    elif username == request.user.username:
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
    fields = ['first_name', 'age', 'sex', 'experience', 'email', 'social_media', 'bio']
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/trails/')

class TripCreate(CreateView):
    model = Trip
    fields = ['date','trail','hiker']
    success_url = '/trips'

@method_decorator(login_required, name='dispatch')
class HikerUpdate(UpdateView):
    model = Hiker
    fields = ['first_name', 'age', 'sex', 'experience', 'email', 'social_media', 'bio']

@method_decorator(login_required, name='dispatch')
class TripsDelete(DeleteView):
    model = Trip
    success_url = '/trips'