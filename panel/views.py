from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse
from urllib.parse import urlencode
from django.db.models import Q
from django.template.defaultfilters import slugify


# importación de funcionalidad para creación de usuarios
from django.contrib.auth.forms import UserCreationForm

# importación de funcionalidad para login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group

# importar custom decorators
from panel.decorators import authenticated_user, allowed_users

# Importar modelos desde apps de backend
# from panel.models import Persona_Model, Ahora_Model, Servicio_Model, Proyecto_Model, Categoria_Proyecto_Model
# from panel.models import Actividad_Academica_Model, Actividad_Laboral_Model, Area_Interes_Model, Tecnologia_Model, Software_Model, Archivo_Model
# from panel.models import Pagina_Model, Articulo_Model, Categoria_Model, Etapa_Model, Imagen_Model
# from panel.models import Mensaje_Contacto_Model, Frontend_Search_Model, Backend_Search_Model, Configuracion_Model

# Importación de forms desde apps de backend
# from panel.forms import Persona_Form, Ahora_Form, Servicio_Form, Proyecto_Form, Categoria_Proyecto_Form
# from panel.forms import Actividad_Academica_Form, Actividad_Laboral_Form, Area_Interes_Form, Tecnologia_Form, Software_Form, Archivo_Form
# from panel.forms import Pagina_Form, Articulo_Form, Categoria_Form, Etapa_Form, Imagen_Form
# from panel.forms import Mensaje_Contacto_Form, Frontend_Search_Form, Backend_Search_Form, Configuracion_Form

from panel.utils import info_header_persona



# =======================================================================================================================================
# Login
# =======================================================================================================================================

@login_required(login_url='entrar')
def test(request, *args, **kwargs):
    '''Test'''

    info_persona = info_header_persona(request)

    context = {
        'page': 'Test',
        #'object_list': object_list,
        'info_persona': info_persona,
    }
    return render(request, 'panel/error_404.html', context)
    #return render(request, 'login/register_user.html', context)



@authenticated_user
def entrar(request, *args, **kwargs):
    '''Página de Login de la plataforma. '''
    # Sacar al usuario que ingresa a esta vista
    #logout(request)

    # Mensajes para el usuario
    status = ''

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # autenticar al usuario
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # loguear al usuario con el usuario recién creado
                login(request, user)
                return redirect('app_panel_index')
            else:
                base_url = reverse('entrar')
                query_string =  urlencode({'status': 'ERROR'})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
                #return redirect('entrar')
        else:
            base_url = reverse('entrar')
            query_string =  urlencode({'status': 'ERROR'})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
            #return redirect('entrar')

    if request.method == 'GET':
        status_get = request.GET.get('status')
        print(f'status_get: {status_get}')
        if status_get == 'ERROR':
            status = 'ERROR'

        status_get = request.GET.get('status')
        print(f'status_get: {status_get}')
        if status_get == 'SALIR':
            status = 'SALIR'

    form = AuthenticationForm()


    context = {
        'page': 'Acceso / Login',
        'status': status,
        'form': form,
    }


    return render(request, 'login/login.html', context)


def salir(request, *args, **kwargs):
    logout(request)
    return redirect('entrar')


