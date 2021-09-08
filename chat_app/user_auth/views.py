from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CreateUserForm
from django.contrib.auth import login, logout, authenticate


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Incorrect username or password')

    if request.user != 'AnonymousUser':
        logoutUser(request)

    return render(request, 'login.html', {})


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'User {user} has been created.')
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')