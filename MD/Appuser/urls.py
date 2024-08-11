from django.urls import path, include
from django.contrib.auth.views import LogoutView
from Appuser import views
from .views import login_request
from .views import cambiarPasswordView2
from .views import editarusuario
from .views import register
from .views import login_request


# http://127.0.0.1:8000/users/
urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('editaru/', views.editarusuario, name="Editaru"),
    path('editarpass/', views.cambiarPasswordView2.as_view(), name="Editarpass"),    
    path('logout/', LogoutView.as_view(template_name="Appuser/logout.html"), name="Logout"),
]