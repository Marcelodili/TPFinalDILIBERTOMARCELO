from django.urls import path, include
from django.contrib.auth.views import LogoutView
from Appuser import views
from .views import login_request

# http://127.0.0.1:8000/users/
urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='Appuser/index.html'), name="Logout")    
#    path("ofertas/listar", views.ofertasListView.as_view(), name="Ofertas."),
#    path("ofertas/edita", views.ofertaseListView.as_view(), name="Ofertase."),
#    path('ofertas/editar/<int:pk>', views.ofertaseUpdateView.as_view(), name="EditarOferta."),
#    path('ofertas/borrar/<int:pk>', views.ofertaseDeleteView.as_view(), name="BorrarOferta."),
#    path("ofertas/detalle/<int:pk>", views.ofertasedListView.as_view(), name="Ofertased."),
#    path("ofertas/agrega", views.ofertaseaCreateView.as_view(), name="Ofertasea.")
]