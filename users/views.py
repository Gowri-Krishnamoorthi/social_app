from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")  # Success message
                return redirect('user_login')  # Stay on the same page or redirect elsewhere
            else:
                messages.error(request, "Wrong credentials. Please try again.")  # Error message
                return redirect('user_login')

    else:
        form = LoginForm()
    
    return render(request, 'users/login.html', {'form': form})
