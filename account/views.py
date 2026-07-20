from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from .forms import SignupForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
        
    return render(request, 'account/signup.html', {'form':form})

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
        
    return render(request, 'account/signin.html', {'form':form})

def signout(request):
    logout(request)
    request.session.flush()
    return redirect('login')