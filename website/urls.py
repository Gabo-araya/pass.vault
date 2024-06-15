from django.urls import path, include
from django.conf.urls.static import static
import website.views

urlpatterns = [

    #páginas
    path('', website.views.inicio, name="inicio"),
    path('blank/', website.views.blank, name="blank"),
    # path('buscar/', website.views.buscar, name="buscar"),

    # path('blog/', website.views.blog, name="blog"),
    # path('articulo/<int:id>/', website.views.articulo, name='articulo'),
    # path('articulo/<str:slug>/', website.views.articulo, name='articulo'),
   
    path('contacto/', website.views.contacto, name="contacto"),
    path('gracias/', website.views.gracias, name="gracias"),

]