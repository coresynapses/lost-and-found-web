from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from lostfound.forms import CustomUserCreationForm
from lostfound.models import CustomUser
from django.urls import reverse


def home(request):
    return render(request, 'home.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or Password")
            return redirect('login')
        else:
            login(request, user)
            return redirect(reverse('lostfound:itemList'))

    return render(request, 'login.html')


def register_page(request):
    '''
        if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(username=username).exists():
            messages.info(request, "Username already taken!")
            return redirect('register')

        user = CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password  # Directly set during creation
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Account created Successfully!")
        return redirect('login')
    '''
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("User registered:", user)  # Debugging
            login(request, user)
            return redirect(reverse('lostfound:itemList'))
        else:
            print("Form errors:", form.errors)  # Debugging
            messages.error(request,'Invalid username or password')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html',{"form": form})

def logout_user(request):
    logout(request)
    return redirect('home')