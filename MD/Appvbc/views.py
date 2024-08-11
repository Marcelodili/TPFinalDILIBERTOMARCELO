from django.shortcuts import render
# <clases basadas en vistas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# clases basadas en vistas>
from App01.models import Destino
from django.urls import reverse_lazy


class ofertasListView(ListView):
    model = Destino
    context_object_name = "ofertas"
    template_name = "Appvbc/ofertas.html"


class ofertaseListView(ListView):
    model = Destino
    context_object_name = "ofertase"
    template_name = "Appvbc/ofertase.html"


class ofertaseUpdateView(UpdateView):
    model = Destino
    template_name = "Appvbc/ofertaseEditar.html"
    success_url = reverse_lazy("Ofertase.")
    fields = ["contacto", "hotel", "precio"]


class ofertaseaCreateView(CreateView):
    model = Destino
    template_name = "Appvbc/ofertaseAgregar.html"
    success_url = reverse_lazy("Ofertasea.")
    fields = ["nombre", "codigo", "contacto", "hotel", "precio", "ubicacion"]


class ofertaseDeleteView(DeleteView):
    model = Destino
    template_name = "Appvbc/ofertaseBorrar.html"
    success_url = reverse_lazy("Ofertase.")
#    success_url = reverse_lazy("BorrarOferta.")


class ofertasedListView(UpdateView):
    model = Destino
    template_name = "Appvbc/ofertaseDetalle.html"
    fields = ["contacto", "hotel", "precio"]

# clases basadas en vistas>
