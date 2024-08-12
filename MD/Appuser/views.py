from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from Appuser.forms import UserRegisterForm, UserEditform
from Appuser.models import Avatar
from django.urls import reverse_lazy
# <clases basadas en vistas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


@login_required
def editarusuario(request):
    usuario = request.user
    if request.method == "POST":
        formulario = UserEditform(request.POST, request.FILES, instance=usuario)
        if formulario.is_valid():
            if formulario.cleaned_data.get("imagen"):
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data.get("imagen"))
                avatar.save()
                #usuario.avatar.imagen = formulario.cleaned_data.get("imagen")
                #usuario.avatar.save()
            formulario.save()
            return render(request, "Appuser/registrook.html")
    else:
        formulario = UserEditform(instance=usuario)
    return render(request, "Appuser/editaru.html", {"form": formulario})


class cambiarPasswordView2(LoginRequiredMixin, PasswordChangeView):
    template_name = "Appuser/editar_pass.html"
    success_url = reverse_lazy("Editaru")


def CerrarUsuario(request):
    logout(request)
    return render(request, "Appuser/logout.html")