from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def home(request):
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Auth
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are in, Cool")
            return redirect('home')
        else:
            messages.success(request, "Nah no go")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You now out")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Auth
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'U good to go')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})