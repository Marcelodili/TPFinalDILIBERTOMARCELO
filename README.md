# TPFinalDILIBERTOMARCELO #

https://1drv.ms/v/c/4f7bee3d37956010/EWMELfsQ3pVCvYhHV4twAgsBImdop_FbJUAwflbBZUFLHA?e=uX4fQr

https://github.com/Marcelodili/TPFinalDILIBERTOMARCELO.git

Ofertas de destinos turísticos e ingreso de solicitud de presupuesto.
Para ingresar un presupuesto primero debe dar de alta el cliente y estar logueado con una cuenta de usuario.

La barra superior de navegación contiene:
    Turismo:     Lleva a la parte superior de la pagina.
    Para vos:    Lleva a la sección "OFERTAS CLIENTES PRESUPUESTOS" como opción a al menú de la barra.
    Nosotros:    Lleva a la sección "NOSOTROS". Contiene botón con vínculo a "/about/"
    Contacto:    Lleva a la sección para enviar mail de contacto. (El botón no realiza la acción real de envío.)
    Inicio:      Vínculo Url.
    Ofertas:     Consulta de destinos turísticos. Vínculo Url.
    Transporte:  Consulta de transportes. Vínculo Url.
    Clientes:     Alta de clientes. Vínculo Url.
    Presupuesto:  Ingreso de solicitud de presupuesto. Vínculo Url.
    Estado:       Consultar estado de presupuesto solicitado: Vínculo Url.
    EditarOfertas:Administración de destinos turísticos.
    Cuenta ingresar o registar
    Logout
    Editar cuenta

# URL accesibles para el proyecto. Detalle.
admin/
    Admin DB.
/
    Home.
about/
    Readme.
users/login/
    Inicio de sesión con usuario y contraseña.
users/register/
    Creación de cuentas de usuario.
users/editaru/
    Edición de datos de cuenta de usuario.
users/editarpass/
    Cambio de contraseña. Enlace desde users/editaru/.
users/logout/
    Cierre de sesion de cuenta de usuario.
ofertas/
vbc/ofertas/listar
    Contenido de tabla APP01_DESTINO.
    No aplica restricción de usuario logueado.
    Permite obtener al cliente los datos para ingresar en la solicitud de presupuesto.
ofertast/
    Contenido de tabla APP01_TRANSPORTES.
    No aplica restricción de usuario logueado.
    Permite obtener al cliente los datos para ingresar en la solicitud de presupuesto.
ingresecliente/
    Accede a tabla APP01_CLIENTE.
    Aplica restricción de usuario logueado.
    Para ingresar una solicitud de presupuesto se necesita datos del cliente, el Dni.
    Un usuario puede tener mas de un cliente.
ingrese/
    Accede a tabla APP01_PRESUPUESTAR.
    Aplica restricción de usuario logueado.
    Permite al cliente ingresar una solicitud de presupuesto.
    Datos requeridos: Dni, nro de codigo de transporte, nro de codigo de destino, comentario, fecha de viaje, cantidad de dias, cantidad de pasajeros.
buscapresupuesto/    
    Accede a tabla APP01_PRESUPUESTAR.
    Aplica restricción de usuario logueado.
    Permite al cliente buscar un presupuesto por Dni.
    Aplica filtro de DNI ingresado y USER logueado.
vbc/ofertas/edita
    Accede a tabla APP01_DESTINO.
    Permite agregar, editar, borrar, detallar registros.
    Aplica restricción de usuario logueado y acceder a:
        vbc/ofertas/detalle/
    Aplica restricción de SUPERusuario logueado y acceder a:
        vbc/ofertas/editar/
        vbc/ofertas/borrar/
        vbc/ofertas/agrega 

# URL accesibles para el proyecto.
admin/
[name='Inicio']
about/ [name='About']
ingrese/ [name='Ingrese']
ofertas/ [name='Ofertas']
ofertast/ [name='OfertasTransporte']
buscapresupuesto/ [name='BuscaPresupuesto']
ingresecliente/ [name='IngreseCliente']
vbc/ofertas/listar [name='Ofertas.']
vbc/ofertas/edita [name='Ofertase.']
vbc/ofertas/agrega [name='Ofertasea.'] 
users/login/ [name='Login']
users/register/ [name='Register']
users/editaru/ [name='Editaru']
users/editarpass/ [name='Editarpass']
users/logout/ [name='Logout'] 
# url complementos para el proyecto
vbc/ ofertas/editar/<int:pk> [name='EditarOferta.']
vbc/ ofertas/borrar/<int:pk> [name='BorrarOferta.']
vbc/ ofertas/detalle/<int:pk> [name='Ofertased.']
^media/(?P<path>.*)$


# URL accesibles fuera del proyecto.
MD01/
MD02/
MD03/<parametro01>
# URL no desarrolladas/incompletas.
MD04/
busqueda/ [name='Busqueda']
buscapresupuestoG/ [name='BuscaPresupuesto']
buscar/

# Tablas del modelo.
APP01_CLIENTE: Campo DNI como valor único. Campo USER obtenido desde AUTH_USER.USERNAME.
APP01_DESTINO: Destinos turísticos ofrecidos.
APP01_TRANSPORTES: Medios de transportes ofrecidos.
APP01_PRESUPUESTAR:Presupuesto solicitado por un Cliente con datos de Destino y Transporte.Campo USER obtenido desde AUTH_USER.USERNAME.
APPUSER_AVATAR: Avatar de usuario. Campo USER_ID obtenido desde AUTH_USER.USERNAME. Repositorio definido en "^media/(?P<path>.*)$"

# Aplicaciones.
App01: aplicación con contenido de template base (_base.html), acceso a datos por funciones.
Appvbc: acceso a datos principalmente por clases.
Appuser: administración de cuentas de usuario.

# Requerimientos del servidor.
Python 3.11.9
django==5.0.7
pip install pillow




