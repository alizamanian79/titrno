from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class SignInView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
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

        context = {"form": form}
        return render(request, 'accounts/login.html', context)

@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You logged out successfully.")
        return redirect('website:index')

class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, 'accounts/signup.html', context)

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You signed up successfully.")
            return redirect('website:index')
        else:
            messages.error(request, "Invalid form submission.")

        context = {"form": form}
        return render(request, 'accounts/signup.html', context)
