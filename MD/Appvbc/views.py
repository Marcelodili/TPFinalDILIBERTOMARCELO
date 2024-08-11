from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# <clases basadas en vistas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from App01.models import Destino



class ofertasListView(ListView):
    model = Destino
    context_object_name = "ofertas"
    template_name = "Appvbc/ofertas.html"


class ofertaseListView(LoginRequiredMixin, ListView):
    model = Destino
    context_object_name = "ofertase"
    template_name = "Appvbc/ofertase.html"


class ofertaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Destino
    template_name = "Appvbc/ofertaseEditar.html"
    success_url = reverse_lazy("Ofertase.")
    fields = ["contacto", "hotel", "precio"]


class ofertaseaCreateView(LoginRequiredMixin, CreateView):
    model = Destino
    template_name = "Appvbc/ofertaseAgregar.html"
    success_url = reverse_lazy("Ofertasea.")
    fields = ["nombre", "codigo", "contacto", "hotel", "precio", "ubicacion"]


class ofertaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Destino
    template_name = "Appvbc/ofertaseBorrar.html"
    success_url = reverse_lazy("Ofertase.")
#    success_url = reverse_lazy("BorrarOferta.")


class ofertasedListView(LoginRequiredMixin, UpdateView):
    model = Destino
    template_name = "Appvbc/ofertaseDetalle.html"
    fields = ["contacto", "hotel", "precio"]

# clases basadas en vistas>
