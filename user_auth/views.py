from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login

def user_login(request):
    return render(request, 'authentication/login.html')

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    authentication_form = AuthenticationForm

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('polls:index')
        else:
            return render(request, 'authentication/login.html', {'error': 'Invalid login credentials'})
    else:
        return redirect('user_auth:login')

def show_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            return redirect('polls:index')
        else:
            return render(request, 'authentication/user.html', {'user': request.user})
    else:
        return redirect('user_auth:login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_auth:registration_success')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

def registration_success(request):
    return render(request, 'authentication/registration_success.html')
