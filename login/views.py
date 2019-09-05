from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, render_to_response, redirect
from login import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_2 = form.cleaned_data['password_2']

            if password == password_2:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
                user.save()
                return HttpResponseRedirect(reverse('register_success'))   
            else:
                error = 'As senhas são diferentes!'
                form = forms.RegistrationForm
                context = {'form': form, 'error': error}

                return render(request, 'registration/register.html', context)
        form = forms.RegistrationForm
        context = {'form': form, }

    else:
        form = forms.RegistrationForm
        context = {'form': form, }

    return render(request,'registration/register.html', context)


def register_success(request):
    return render_to_response('registration/sucess.html', {})

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))

        else:
            form = forms.LoginForm
    else:
        form = forms.LoginForm
    context = {'form': form, }
    return render(request, 'registration/login.html', context)
