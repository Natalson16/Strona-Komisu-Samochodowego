from django.shortcuts import render, redirect
from .models import Samochod, Marka, Model
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def registerPage(request):
    if request.user.is_authenticated:
        return redirect(home)
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Twoje konto zostało utworzone!')
                return redirect(loginPage)

        dane = {'form': form}
        return render(request, 'rejestracja.html', dane)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect(home)
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(home)
            else:
                messages.info(request, 'Nazwa użytkownika lub hasło jest nieprawidłowe')

        dane = {}
        return render(request, 'logowanie.html', dane)

def logoutUser(request):
    logout(request)
    return redirect(loginPage)


@login_required(login_url='logowanie')
def home(request):
    url = 'http://127.0.0.1:8000/'
    marki = Marka.objects.all()
    dane = {'marki': marki,
            'url': url}
    return render(request, 'home.html', dane)

@login_required(login_url='logowanie')
def main(request):
    url = 'http://127.0.0.1:8000/'
    marki = Marka.objects.all()
    dane = {'marki': marki,
            'url': url}
    return render(request, 'main.html', dane)

@login_required(login_url='logowanie')
def marka(request, id):
    marki = Marka.objects.all()
    marka = Marka.objects.get(pk=id)
    modele = Model.objects.filter(marka=marka)
    dane = {'marka': marka,
            'marki': marki,
            'modele': modele}
    return render(request, 'marka.html', dane)

def model(request, id):
    marki = Marka.objects.all()
    model = Model.objects.get(pk=id)
    samochody = Samochod.objects.filter(model=model)
    dane = {'marki': marki,
            'model': model,
            'samochody': samochody}
    return render(request, 'model.html', dane)

@login_required(login_url='logowanie')
def samochod(request, id):
    samochod = Samochod.objects.get(pk=id)
    marki = Marka.objects.all()
    dane = {'marki': marki,
            'samochod': samochod}
    return render(request, 'samochod.html', dane)





