from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index(request):
    # Handle both GET and POST requests for the registration form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('index')  # Redirect back to the homepage after successful registration
    else:
        form = UserCreationForm()  # Display an empty form for GET requests

    # form passed to django template
    return render(request, 'index.html', {'form': form})