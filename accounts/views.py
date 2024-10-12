from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def signIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You logged in successfully.")
                return redirect('/')
            else:
                messages.error(request, "Your username and password are incorrect.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, 'accounts/login.html', context)

@login_required
def logoutView(request):
    logout(request)
    messages.success(request, "You logged out successfully.")
    return redirect('website:index') 


def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You signed up successfully.")
            return redirect('website:index')
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, 'accounts/signup.html', context)