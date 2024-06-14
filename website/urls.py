from django.urls import path, include
from django.conf.urls.static import static
import website.views

urlpatterns = [

    #páginas
    path('', website.views.inicio, name="inicio"),
    # path('blank/', website.views.blank, name="blank"),
    # path('buscar/', website.views.buscar, name="buscar"),

    # path('blog/', website.views.blog, name="blog"),
    # path('articulo/<int:id>/', website.views.articulo, name='articulo'),
    # path('articulo/<str:slug>/', website.views.articulo, name='articulo'),

    # path('portafolio/', website.views.portafolio, name="portafolio"),
    # path('proyecto/<str:slug>/', website.views.proyecto, name='proyecto'),

    # path('notas_ahora/', website.views.notas_ahora, name="notas_ahora"),
    # path('nota/<int:id>/', website.views.nota, name='nota'),

    path('contacto/', website.views.contacto, name="contacto"),
    # path('perfil_profesional/', website.views.perfil_profesional, name="perfil_profesional"),
    # path('perfil_academico/', website.views.perfil_academico, name="perfil_academico"),
    path('gracias/', website.views.gracias, name="gracias"),

]