from django.urls import path, include
from Appvbc import views

# http://127.0.0.1:8000/vbc/ofertas/listar
urlpatterns = [
    path("ofertas/listar", views.ofertasListView.as_view(), name="Ofertas."),
    path("ofertas/edita", views.ofertaseListView.as_view(), name="Ofertase."),
    path('ofertas/editar/<int:pk>', views.ofertaseUpdateView.as_view(), name="EditarOferta."),
    path('ofertas/borrar/<int:pk>', views.ofertaseDeleteView.as_view(), name="BorrarOferta."),
    path("ofertas/detalle/<int:pk>", views.ofertasedListView.as_view(), name="Ofertased."),
    path("ofertas/agrega", views.ofertaseaCreateView.as_view(), name="Ofertasea.")
]