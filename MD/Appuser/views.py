from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from Appuser.forms import UserRegisterForm
# <clases basadas en vistas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from App01.models import Destino
# Create your views here.


def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                next_url = request.GET.get("next", "/")
                return HttpResponseRedirect(next_url)
        msg_login = "Usuario o contraseña incorrecto"
    form = AuthenticationForm()
    return render(request, "Appuser/login.html", {"form": form, "msg_login": msg_login})


def register(request):
    msg_register = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            msg_register = "Registracion correcta"
            return render(request, "Appuser/registrook.html")
        msg_register = "Error en los datos ingresados"
    else:
        form = UserRegisterForm()
    return render(request, "Appuser/registro.html",  {"form": form, "msg_register": msg_register})

