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



# =======================================================================================================================================
# Vista de inicio
# =======================================================================================================================================

@login_required(login_url='entrar')
def app_panel_index(request, *args, **kwargs):
    '''Lista de elementos con las que se pueden realizar acciones.'''

    elementos_website = [
        {
            'object_title': 'Artículos',
            'icon': 'bi bi-file-richtext',
            'object_description': 'Agregar, modificar o eliminar articulos.',
            'url_listar': 'listar_articulos',
            'url_crear': 'crear_articulo',
        },
        {
            'object_title': 'Imágenes',
            'icon': 'bi bi-images',
            'object_description': 'Agregar, modificar o eliminar imagen.',
            'url_listar': 'listar_imagenes',
            'url_crear': 'crear_imagen',
        },
    ]

    elementos_website_password = [
        {
            'object_title': 'Categorías de Password',
            'icon': 'bi bi-tags',
            'object_description': 'Agregar, modificar o eliminar categorías de passwords.',
            'url_listar': 'listar_categorias_proyecto',
            'url_crear': 'crear_categoria_proyecto',
        },
        {
            'object_title': 'Password',
            'icon': 'bi bi-tags',
            'object_description': 'Agregar, modificar o eliminar passwords.',
            'url_listar': 'listar_passwords',
            'url_crear': 'crear_password',
        },
    ]

    elementos_funcionalidades = [
        {
            'object_title': 'Mensajes de contacto',
            'icon': 'bi bi-envelope-paper-heart',
            'object_description': 'Revisar o eliminar mensajesde contacto.',
            'url_listar': 'listar_mensajes_contacto',
        },
        {
            'object_title': 'Búsqueda de panel admin',
            'icon': 'bi bi-search',
            'object_description': 'Revisar o eliminar búsquedas realizadas en el panel de administración.',
            'url_listar': 'listar_busquedas_backend',
        },
    ]

    elementos_configuracion = [
        {
            'object_title': 'Perfil',
            'icon': 'bi bi-person',
            'object_description': 'Modificar perfil.',
            'url_listar': 'ver_perfil',
        },
        {
            'object_title': 'Categorías de Artículos',
            'icon': 'bi bi-tags',
            'object_description': 'Agregar, modificar o eliminar categorías de artículos.',
            'url_listar': 'listar_categorias',
            'url_crear': 'crear_categoria',
        },
        {
            'object_title': 'Etapas',
            'icon': 'bi bi-speedometer2',
            'object_description': 'Agregar, modificar o eliminar etapas.',
            'url_listar': 'listar_etapas',
            'url_crear': 'crear_etapa',
        },
        {
            'object_title': 'Configuración',
            'icon': 'bi bi-gear',
            'object_description': 'Modificar configuración.',
            'url_listar': 'ver_configuracion',
        },
    ]


    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name

    count_ahora = Ahora_Model.objects.filter(borrador=False).count()
    count_proyectos = Proyecto_Model.objects.all().count()
    count_proyectos_activos = Proyecto_Model.objects.filter(borrador=False).count()
    count_proyectos_inactivos = Proyecto_Model.objects.filter(borrador=True).count()
    count_servicios = Servicio_Model.objects.all().count()
    count_servicios_activos = Servicio_Model.objects.filter(borrador=False).count()
    count_servicios_inactivos = Servicio_Model.objects.filter(borrador=True).count()
    count_articulos = Articulo_Model.objects.all().count()
    count_articulos_activos = Articulo_Model.objects.filter(borrador=False).count()
    count_articulos_inactivos = Articulo_Model.objects.filter(borrador=True).count()

    # Lista Actividades Académicas
    lista_actividades_academicas = Actividad_Academica_Model.objects.filter(borrador=False).order_by('-fecha')[:5]
    # Lista Actividades Laborales
    lista_actividades_laborales = Actividad_Laboral_Model.objects.filter(borrador=False).order_by('-fecha')[:5]
    # Lista Areas de Interés
    lista_areas_interes = Area_Interes_Model.objects.filter(borrador=False).order_by('-created')[:5]

    # Lista Tecnologías
    lista_tecnologias = Tecnologia_Model.objects.filter(borrador=False).order_by('-created')[:5]
    # Lista Software
    lista_software = Software_Model.objects.filter(borrador=False).order_by('-created')[:5]
    # Lista Mensaje Contacto
    listar_mensajes_contacto = Mensaje_Contacto_Model.objects.all().order_by('-created')[:5]

    user_actual = request.user.id
    print(f'user_actual: {request.user}')

    count_mensajes_contacto = listar_mensajes_contacto.count()

    info_persona = info_header_persona(request)
    #print(f'info_persona: {info_persona}')


    context = {
        'page': 'Inicio',
        'icon': 'bi bi-grid',
        'count_ahora': count_ahora,
        'count_articulos': count_articulos,
        'count_articulos_activos': count_articulos_activos,
        'count_articulos_inactivos': count_articulos_inactivos,
        'count_proyectos': count_proyectos,
        'count_proyectos_activos': count_proyectos_activos,
        'count_proyectos_inactivos': count_proyectos_inactivos,
        'count_servicios': count_servicios,
        'count_servicios_activos': count_servicios_activos,
        'count_servicios_inactivos': count_servicios_inactivos,
        'lista_actividades_academicas': lista_actividades_academicas,
        'lista_actividades_laborales': lista_actividades_laborales,
        'lista_areas_interes': lista_areas_interes,
        'lista_tecnologias': lista_tecnologias,
        'lista_software': lista_software,
        'listar_mensajes_contacto': listar_mensajes_contacto,
        'user_actual': user_actual,
        'count_mensajes_contacto': count_mensajes_contacto,
        'info_persona': info_persona,
        'info_configuracion': info_configuracion(),
        'elementos_curriculum': elementos_curriculum,
        'elementos_website': elementos_website,
        'elementos_funcionalidades': elementos_funcionalidades,
        'elementos_configuracion': elementos_configuracion,
    }
    if group == 'admin':
        return render(request, 'panel/app_index.html', context)
    elif group == 'agent':
        return render(request, 'panel/dashboard_agent.html', context)
    elif group == None:
        return redirect('salir')



#----------------------------------------------------------------------
# Resultados_Busqueda
#----------------------------------------------------------------------

@login_required(login_url='entrar')
def resultados_busqueda(request, *args, **kwargs):
    '''Muestra resultados de búsqueda.'''
    form = Busqueda_Panel_Form()
    vacio = True
    termino_busqueda = ''
    
    result_ahora = ''
    result_servicio = ''
    result_proyecto = ''
    result_categoria_proyecto = ''
    
    result_actividad_academica = ''
    result_actividad_laboral = ''
    result_area_interes = ''
    
    result_tecnologia = ''
    result_software = ''
    result_archivo = ''
    
    result_pagina = ''
    result_articulo = ''
    result_categoria = ''
    result_etapa = ''
    result_imagen = ''
    result_mensaje_contacto = ''
    
    if request.method == 'POST':
        form = Busqueda_Panel_Form(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['name']
            print(termino_busqueda)
            #form.save()

        if termino_busqueda == '':
            vacio = True
        else:
            vacio = False
            
            # result_ahora = Ticket_Model.objects.distinct().filter(
            #     Q(nombre__icontains=termino_busqueda) |  
            #     Q(contenido__icontains=termino_busqueda)
            #     )
    
    context = {
        'page': 'Resultados de búsqueda',
        'icon': 'bi bi-grid',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'termino_busqueda': termino_busqueda,
        'vacio': vacio,
        'result_ahora': result_ahora,
        'result_servicio': result_servicio,
        'result_proyecto': result_proyecto,
        'result_categoria_proyecto': result_categoria_proyecto,
        'result_actividad_academica': result_actividad_academica,
        'result_actividad_laboral': result_actividad_laboral,
        'result_area_interes': result_area_interes,
        'result_tecnologia': result_tecnologia,
        'result_software': result_software,
        'result_archivo': result_archivo,
        'result_pagina': result_pagina,
        'result_articulo': result_articulo,
        'result_categoria': result_categoria,
        'result_etapa': result_etapa,
        'result_imagen': result_imagen,
        'result_mensaje_contacto': result_mensaje_contacto,
    }
    return render(request, 'panel/search_result.html', context)




#----------------------------------------------------------------------
# Password
#----------------------------------------------------------------------


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def listar_password(request, *args, **kwargs):
    '''Lista de Password.'''
    
    # Mensajes para el usuario
    success_create = ''
    success_edit = ''
    success_activate = ''
    success_deactivate = ''
    success_delete = ''
    if request.method == 'GET':
        success_create_get = request.GET.get('success_create')
        print(f'success_create_get: {success_create_get}')
        if success_create_get == 'OK':
            success_create = 'OK'
        success_edit_get = request.GET.get('success_edit')
        print(f'success_edit_get: {success_edit_get}')
        if success_edit_get == 'OK':
            success_edit = 'OK'
        success_activate_get = request.GET.get('success_activate')
        print(f'success_activate_get: {success_activate_get}')
        if success_activate_get == 'OK':
            success_activate = 'OK'
        success_deactivate_get = request.GET.get('success_deactivate')
        print(f'success_deactivate_get: {success_deactivate_get}')
        if success_deactivate_get == 'OK':
            success_deactivate = 'OK'
        success_delete_get = request.GET.get('success_delete')
        print(f'success_delete_get: {success_delete_get}')
        if success_delete_get == 'OK':
            success_delete = 'OK'
    
    queryset = Password_Model.objects.filter(activo=True) # Lista de objetos
    cantidad = queryset.count() #necesario para el total
    paginator = Paginator(queryset, cantidad_elementos) 
    page_number = request.GET.get('pag')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page' : 'Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'password',
        'plural' : 'passwords',
        'url_listar_activo' : 'listar_password',
        'url_listar_inactivo' : 'listar_password_inactivo',
        'url_crear' : 'crear_password',
        'url_ver' : 'ver_password',
        'url_editar' : 'modificar_password',
        'url_desactivar' : 'desactivar_password',
        'url_activar' : 'activar_password',
        'url_eliminar' : 'eliminar_password',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_activate': success_activate,
        'success_deactivate': success_deactivate,
        'success_delete': success_delete,
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'cantidad': cantidad,
        'object_list': page_obj
    }
    return render(request, 'panel/listar_objetos.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def listar_password_inactivo(request, *args, **kwargs):
    '''Lista de Password inactivos.'''

    queryset = Password_Model.objects.filter(activo=False) # Lista de objetos
    cantidad = queryset.count() #necesario para el total
    paginator = Paginator(queryset, cantidad_elementos) 
    page_number = request.GET.get('pag')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page' : 'Basurero de Password',
        'icon' : 'delete_outline',
        'color' : 'info',
        'singular' : 'password',
        'plural' : 'passwords',
        'url_listar_activo' : 'listar_password',
        'url_listar_inactivo' : 'listar_password_inactivo',
        'url_crear' : 'crear_password',
        'url_ver' : 'ver_password',
        'url_editar' : 'modificar_password',
        'url_desactivar' : 'desactivar_password',
        'url_activar' : 'activar_password',
        'url_eliminar' : 'eliminar_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'cantidad': cantidad,
        'object_list': page_obj
    }
    return render(request, 'panel/listar_objetos.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def ver_password(request, id, *args, **kwargs):
    '''Revisar Password.'''
    
    # Mensajes para el usuario
    success_create = ''
    success_edit = ''
    success_activate = ''
    success_deactivate = ''
    success_delete = ''
    if request.method == 'GET':
        success_create_get = request.GET.get('success_create')
        print(f'success_create_get: {success_create_get}')
        if success_create_get == 'OK':
            success_create = 'OK'
        success_edit_get = request.GET.get('success_edit')
        print(f'success_edit_get: {success_edit_get}')
        if success_edit_get == 'OK':
            success_edit = 'OK'
        success_activate_get = request.GET.get('success_activate')
        print(f'success_activate_get: {success_activate_get}')
        if success_activate_get == 'OK':
            success_activate = 'OK'
        success_deactivate_get = request.GET.get('success_deactivate')
        print(f'success_deactivate_get: {success_deactivate_get}')
        if success_deactivate_get == 'OK':
            success_deactivate = 'OK'
        success_delete_get = request.GET.get('success_delete')
        print(f'success_delete_get: {success_delete_get}')
        if success_delete_get == 'OK':
            success_delete = 'OK'
    
    itemObj = Password_Model.objects.get(id=id)
    contactos_password = Contacto_Model.objects.filter(fk_password=itemObj.id).filter(activo=True)
    
    context = {
        'page' : 'Revisar Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'password',
        'plural' : 'passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_password',
        'url_listar_activo' : 'listar_password',
        'url_listar_inactivo' : 'listar_password_inactivo',
        'url_crear' : 'crear_password',
        'url_ver' : 'ver_password',
        'url_editar' : 'modificar_password',
        'url_desactivar' : 'desactivar_password',
        'url_activar' : 'activar_password',
        'url_eliminar' : 'eliminar_password',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_activate': success_activate,
        'success_deactivate': success_deactivate,
        'success_delete': success_delete,
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'item': itemObj,
        'contactos': contactos_password,
    }
    return render(request, 'panel/detalle_objeto.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def crear_password(request, *args, **kwargs):
    '''Crear Password.'''
    
    form = Password_Form

    if request.method == 'POST':
        form = Password_Form(request.POST)
        if form.is_valid():
            form.save()

            #guardar historial
            itemObj = Password_Model.objects.latest('created')
            contenido_inicial = [
                #campos genéricos
                ['id', itemObj.id],
                # ['activo', itemObj.activo],
                ['created', itemObj.created],
                ['updated', itemObj.updated],
                ['deleted', itemObj.deleted],
                #campos elemento
                ['nombre', itemObj.nombre],
                ['descripcion', itemObj.descripcion],
                ['fk_organizacion', itemObj.fk_organizacion],
                ['observaciones', itemObj.observaciones],
            ]
            histObj = Accion_Model(
                accion = 'Crear Password',
                usuario = request.user,
                id_elemento = itemObj.id,
                nombre_elemento = itemObj.nombre,
                tipo_elemento = 'DEPARTAMENTO',
                tipo_accion = 'CREAR',
                descripcion = str('El Password [{}] {} fue creado.'.format(itemObj.id,itemObj.nombre)),
                contenido_inicial = contenido_inicial,
                created = datetime.datetime.now(),
                activo = '1'
            )
            histObj.save()

            id_fk_organizacion = str(itemObj.fk_organizacion.id)
            print(f'id_fk_organizacion: {id_fk_organizacion}')
            base_url = reverse('ver_organizacion', args=(id_fk_organizacion,))
            query_string =  urlencode({'success_create': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            #return redirect('listar_password')

    context = {
        'page' : 'Crear Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'password',
        'plural' : 'passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'form': form
    }
    return render(request, 'panel/generic_form.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def modificar_password(request, id, *args, **kwargs):
    '''Modificar Password.'''
    
    itemObj = Password_Model.objects.get(id=id)
    form = Password_Form(instance=itemObj)

    if request.method == 'POST':
        form = Password_Form(request.POST, instance=itemObj)
        if form.is_valid():

            #guardar historial  
            #campos del modelo 
            contenido_anterior = [
                #campos genéricos
                ['id', itemObj.id],
                # ['activo', itemObj.activo],
                ['created', itemObj.created],
                ['updated', itemObj.updated],
                ['deleted', itemObj.deleted],
                #campos elemento
                ['nombre', itemObj.nombre],
                ['descripcion', itemObj.descripcion],
                ['fk_organizacion', itemObj.fk_organizacion],
                ['observaciones', itemObj.observaciones],
            ]
            contenido_actual = [
                #campos genéricos
                ['id', itemObj.id],
                # # ['activo', form.cleaned_data['activo']],
                # campos elemento
                ['nombre', form.cleaned_data['nombre']],
                ['descripcion', form.cleaned_data['descripcion']],
                ['fk_organizacion', form.cleaned_data['fk_organizacion']],
                ['observaciones', form.cleaned_data['observaciones']],
            ]
            #crear objeto con los datos antiguos y guardarlo en el historial      
            histObj = Accion_Model(
                accion = 'Modificar Password',
                usuario = request.user,
                id_elemento = itemObj.id,
                nombre_elemento = itemObj.nombre,
                tipo_elemento = 'DEPARTAMENTO',
                tipo_accion = 'MODIFICAR',
                descripcion = str('El Password [{}] {} fue modificado.'.format(itemObj.id,itemObj.nombre)),
                contenido_anterior = contenido_anterior,
                contenido_actual = contenido_actual,
                created = datetime.datetime.now(),
                activo = '1'
            )
            histObj.save()

            form.save()
            
            id_fk_organizacion = str(itemObj.fk_organizacion.id)
            print(f'id_fk_organizacion: {id_fk_organizacion}')
            base_url = reverse('ver_organizacion', args=(id_fk_organizacion,))
            query_string =  urlencode({'success_edit': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            return redirect('listar_password')

    context = {
        'page' : 'Modificar Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'password',
        'plural' : 'passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'form': form
    }
    return render(request, 'panel/generic_form.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def activar_password(request, id, *args, **kwargs):
    '''Activar Password.'''
    
    itemObj = Password_Model.objects.get(id=id)

    if request.method == 'POST':
        itemObj.activo = '1'
        itemObj.deleted = None
        
        #guardar historial        
        histObj = Accion_Model(
            accion = 'Activar Password',
            usuario = request.user,
            id_elemento = itemObj.id,
            nombre_elemento = itemObj.nombre,
            tipo_elemento = 'DEPARTAMENTO',
            tipo_accion = 'ACTIVAR',
            descripcion = str('El Password [{}] {} fue activado.'.format(itemObj.id,itemObj.nombre)),
            created = datetime.datetime.now(),
            activo = '1'
        )
        histObj.save()

        itemObj.save()
        
        id_fk_organizacion = str(itemObj.fk_organizacion.id)
        print(f'id_fk_organizacion: {id_fk_organizacion}')
        base_url = reverse('ver_organizacion', args=(id_fk_organizacion,))
        query_string =  urlencode({'success_activate': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        #return redirect('listar_password')

    context = {
        'page' : 'Activar Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'password',
        'plural' : 'passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'item': itemObj
    }
    return render(request, 'panel/activar_objetos.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def desactivar_password(request, id, *args, **kwargs):
    '''Desactivar Password.'''
    
    itemObj = Password_Model.objects.get(id=id)

    if request.method == 'POST':
        itemObj.activo = '0'
        itemObj.deleted = datetime.datetime.now()

        #guardar historial        
        histObj = Accion_Model(
            accion = 'Desactivar Password',
            usuario = request.user,
            id_elemento = itemObj.id,
            nombre_elemento = itemObj.nombre,
            tipo_elemento = 'DEPARTAMENTO',
            tipo_accion = 'DESACTIVAR',
            descripcion = str('El Password [{}] {} fue desactivado.'.format(itemObj.id,itemObj.nombre)),
            created = datetime.datetime.now(),
            activo = '1'
        )
        histObj.save()

        itemObj.save()
        
        id_fk_organizacion = str(itemObj.fk_organizacion.id)
        print(f'id_fk_organizacion: {id_fk_organizacion}')
        base_url = reverse('ver_organizacion', args=(id_fk_organizacion,))
        query_string =  urlencode({'success_deactivate': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        #return redirect('listar_password')

    context = {
        'page' : 'Desactivar Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'password',
        'plural' : 'passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'item': itemObj
    }
    return render(request, 'panel/desactivar_objetos.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def eliminar_password(request, id, *args, **kwargs):
    '''Eliminar Password.'''
    
    itemObj = Password_Model.objects.get(id=id)
    
    if request.method == 'POST':

        #guardar historial 
        contenido_eliminado = [
            #campos genéricos
            ['id', itemObj.id],
            # ['activo', itemObj.activo],
            ['created', itemObj.created],
            ['updated', itemObj.updated],
            ['deleted', itemObj.deleted],
            #campos elemento
            ['nombre', itemObj.nombre],
            ['descripcion', itemObj.descripcion],
            ['fk_organizacion', itemObj.fk_organizacion],
            ['observaciones', itemObj.observaciones],
        ]
    
        histObj = Accion_Model(
            accion = 'Eliminar Password',
            usuario = request.user,
            id_elemento = itemObj.id,
            nombre_elemento = itemObj.nombre,
            tipo_elemento = 'DEPARTAMENTO',
            tipo_accion = 'ELIMINAR',
            descripcion = str('El Password [{}] {} fue eliminado.'.format(itemObj.id,itemObj.nombre)),
            contenido_eliminado = contenido_eliminado,
            created = datetime.datetime.now(),
            activo = '1'
        )
        histObj.save()

        itemObj.delete()
        
        id_fk_organizacion = str(itemObj.fk_organizacion.id)
        print(f'id_fk_organizacion: {id_fk_organizacion}')
        base_url = reverse('ver_organizacion', args=(id_fk_organizacion,))
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        #return redirect('listar_password')

    context = {
        'page' : 'Eliminar Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'password',
        'plural' : 'passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'item': itemObj
    }
    return render(request, 'panel/eliminar_objetos.html', context)



#----------------------------------------------------------------------
# Categoría Password
#----------------------------------------------------------------------


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def listar_categoria_password(request, *args, **kwargs):
    '''Lista de Password.'''
    
    # Mensajes para el usuario
    success_create = ''
    success_edit = ''
    success_activate = ''
    success_deactivate = ''
    success_delete = ''
    if request.method == 'GET':
        success_create_get = request.GET.get('success_create')
        print(f'success_create_get: {success_create_get}')
        if success_create_get == 'OK':
            success_create = 'OK'
        success_edit_get = request.GET.get('success_edit')
        print(f'success_edit_get: {success_edit_get}')
        if success_edit_get == 'OK':
            success_edit = 'OK'
        success_activate_get = request.GET.get('success_activate')
        print(f'success_activate_get: {success_activate_get}')
        if success_activate_get == 'OK':
            success_activate = 'OK'
        success_deactivate_get = request.GET.get('success_deactivate')
        print(f'success_deactivate_get: {success_deactivate_get}')
        if success_deactivate_get == 'OK':
            success_deactivate = 'OK'
        success_delete_get = request.GET.get('success_delete')
        print(f'success_delete_get: {success_delete_get}')
        if success_delete_get == 'OK':
            success_delete = 'OK'
    
    queryset = Password_Model.objects.filter(activo=True) # Lista de objetos
    cantidad = queryset.count() #necesario para el total
    paginator = Paginator(queryset, cantidad_elementos) 
    page_number = request.GET.get('pag')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page' : 'Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'categoria_password',
        'plural' : 'categoria_passwords',
        'url_listar_activo' : 'listar_categoria_password',
        'url_listar_inactivo' : 'listar_categoria_password_inactivo',
        'url_crear' : 'crear_categoria_password',
        'url_ver' : 'ver_categoria_password',
        'url_editar' : 'modificar_categoria_password',
        'url_desactivar' : 'desactivar_categoria_password',
        'url_activar' : 'activar_categoria_password',
        'url_eliminar' : 'eliminar_categoria_password',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_activate': success_activate,
        'success_deactivate': success_deactivate,
        'success_delete': success_delete,
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'cantidad': cantidad,
        'object_list': page_obj
    }
    return render(request, 'panel/listar_objetos.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def listar_categoria_password_inactivo(request, *args, **kwargs):
    '''Lista de Password inactivos.'''

    queryset = Password_Model.objects.filter(activo=False) # Lista de objetos
    cantidad = queryset.count() #necesario para el total
    paginator = Paginator(queryset, cantidad_elementos) 
    page_number = request.GET.get('pag')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page' : 'Basurero de Password',
        'icon' : 'delete_outline',
        'color' : 'info',
        'singular' : 'categoria_password',
        'plural' : 'categoria_passwords',
        'url_listar_activo' : 'listar_categoria_password',
        'url_listar_inactivo' : 'listar_categoria_password_inactivo',
        'url_crear' : 'crear_categoria_password',
        'url_ver' : 'ver_categoria_password',
        'url_editar' : 'modificar_categoria_password',
        'url_desactivar' : 'desactivar_categoria_password',
        'url_activar' : 'activar_categoria_password',
        'url_eliminar' : 'eliminar_categoria_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'cantidad': cantidad,
        'object_list': page_obj
    }
    return render(request, 'panel/listar_objetos.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def ver_categoria_password(request, id, *args, **kwargs):
    '''Revisar Password.'''
    
    # Mensajes para el usuario
    success_create = ''
    success_edit = ''
    success_activate = ''
    success_deactivate = ''
    success_delete = ''
    if request.method == 'GET':
        success_create_get = request.GET.get('success_create')
        print(f'success_create_get: {success_create_get}')
        if success_create_get == 'OK':
            success_create = 'OK'
        success_edit_get = request.GET.get('success_edit')
        print(f'success_edit_get: {success_edit_get}')
        if success_edit_get == 'OK':
            success_edit = 'OK'
        success_activate_get = request.GET.get('success_activate')
        print(f'success_activate_get: {success_activate_get}')
        if success_activate_get == 'OK':
            success_activate = 'OK'
        success_deactivate_get = request.GET.get('success_deactivate')
        print(f'success_deactivate_get: {success_deactivate_get}')
        if success_deactivate_get == 'OK':
            success_deactivate = 'OK'
        success_delete_get = request.GET.get('success_delete')
        print(f'success_delete_get: {success_delete_get}')
        if success_delete_get == 'OK':
            success_delete = 'OK'
    
    itemObj = Password_Model.objects.get(id=id)
    contactos_categoria_password = Contacto_Model.objects.filter(fk_categoria_password=itemObj.id).filter(activo=True)
    
    context = {
        'page' : 'Revisar Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'categoria_password',
        'plural' : 'categoria_passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_categoria_password',
        'url_listar_activo' : 'listar_categoria_password',
        'url_listar_inactivo' : 'listar_categoria_password_inactivo',
        'url_crear' : 'crear_categoria_password',
        'url_ver' : 'ver_categoria_password',
        'url_editar' : 'modificar_categoria_password',
        'url_desactivar' : 'desactivar_categoria_password',
        'url_activar' : 'activar_categoria_password',
        'url_eliminar' : 'eliminar_categoria_password',
        'success_create': success_create,
        'success_edit': success_edit,
        'success_activate': success_activate,
        'success_deactivate': success_deactivate,
        'success_delete': success_delete,
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'item': itemObj,
        'contactos': contactos_categoria_password,
    }
    return render(request, 'panel/detalle_objeto.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def crear_categoria_password(request, *args, **kwargs):
    '''Crear Password.'''
    
    form = Password_Form

    if request.method == 'POST':
        form = Password_Form(request.POST)
        if form.is_valid():
            form.save()

            #guardar historial
            itemObj = Password_Model.objects.latest('created')
            contenido_inicial = [
                #campos genéricos
                ['id', itemObj.id],
                # ['activo', itemObj.activo],
                ['created', itemObj.created],
                ['updated', itemObj.updated],
                ['deleted', itemObj.deleted],
                #campos elemento
                ['nombre', itemObj.nombre],
                ['descripcion', itemObj.descripcion],
                ['fk_organizacion', itemObj.fk_organizacion],
                ['observaciones', itemObj.observaciones],
            ]
            histObj = Accion_Model(
                accion = 'Crear Password',
                usuario = request.user,
                id_elemento = itemObj.id,
                nombre_elemento = itemObj.nombre,
                tipo_elemento = 'DEPARTAMENTO',
                tipo_accion = 'CREAR',
                descripcion = str('El Password [{}] {} fue creado.'.format(itemObj.id,itemObj.nombre)),
                contenido_inicial = contenido_inicial,
                created = datetime.datetime.now(),
                activo = '1'
            )
            histObj.save()

            id_fk_organizacion = str(itemObj.fk_organizacion.id)
            print(f'id_fk_organizacion: {id_fk_organizacion}')
            base_url = reverse('ver_organizacion', args=(id_fk_organizacion,))
            query_string =  urlencode({'success_create': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            #return redirect('listar_categoria_password')

    context = {
        'page' : 'Crear Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'categoria_password',
        'plural' : 'categoria_passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_categoria_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'form': form
    }
    return render(request, 'panel/generic_form.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def modificar_categoria_password(request, id, *args, **kwargs):
    '''Modificar Password.'''
    
    itemObj = Password_Model.objects.get(id=id)
    form = Password_Form(instance=itemObj)

    if request.method == 'POST':
        form = Password_Form(request.POST, instance=itemObj)
        if form.is_valid():

            #guardar historial  
            #campos del modelo 
            contenido_anterior = [
                #campos genéricos
                ['id', itemObj.id],
                # ['activo', itemObj.activo],
                ['created', itemObj.created],
                ['updated', itemObj.updated],
                ['deleted', itemObj.deleted],
                #campos elemento
                ['nombre', itemObj.nombre],
                ['descripcion', itemObj.descripcion],
                ['fk_organizacion', itemObj.fk_organizacion],
                ['observaciones', itemObj.observaciones],
            ]
            contenido_actual = [
                #campos genéricos
                ['id', itemObj.id],
                # # ['activo', form.cleaned_data['activo']],
                # campos elemento
                ['nombre', form.cleaned_data['nombre']],
                ['descripcion', form.cleaned_data['descripcion']],
                ['fk_organizacion', form.cleaned_data['fk_organizacion']],
                ['observaciones', form.cleaned_data['observaciones']],
            ]
            #crear objeto con los datos antiguos y guardarlo en el historial      
            histObj = Accion_Model(
                accion = 'Modificar Password',
                usuario = request.user,
                id_elemento = itemObj.id,
                nombre_elemento = itemObj.nombre,
                tipo_elemento = 'DEPARTAMENTO',
                tipo_accion = 'MODIFICAR',
                descripcion = str('El Password [{}] {} fue modificado.'.format(itemObj.id,itemObj.nombre)),
                contenido_anterior = contenido_anterior,
                contenido_actual = contenido_actual,
                created = datetime.datetime.now(),
                activo = '1'
            )
            histObj.save()

            form.save()
            
            id_fk_organizacion = str(itemObj.fk_organizacion.id)
            print(f'id_fk_organizacion: {id_fk_organizacion}')
            base_url = reverse('ver_organizacion', args=(id_fk_organizacion,))
            query_string =  urlencode({'success_edit': 'OK'})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
            return redirect('listar_categoria_password')

    context = {
        'page' : 'Modificar Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'categoria_password',
        'plural' : 'categoria_passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_categoria_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'form': form
    }
    return render(request, 'panel/generic_form.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def activar_categoria_password(request, id, *args, **kwargs):
    '''Activar Password.'''
    
    itemObj = Password_Model.objects.get(id=id)

    if request.method == 'POST':
        itemObj.activo = '1'
        itemObj.deleted = None
        
        #guardar historial        
        histObj = Accion_Model(
            accion = 'Activar Password',
            usuario = request.user,
            id_elemento = itemObj.id,
            nombre_elemento = itemObj.nombre,
            tipo_elemento = 'DEPARTAMENTO',
            tipo_accion = 'ACTIVAR',
            descripcion = str('El Password [{}] {} fue activado.'.format(itemObj.id,itemObj.nombre)),
            created = datetime.datetime.now(),
            activo = '1'
        )
        histObj.save()

        itemObj.save()
        
        id_fk_organizacion = str(itemObj.fk_organizacion.id)
        print(f'id_fk_organizacion: {id_fk_organizacion}')
        base_url = reverse('ver_organizacion', args=(id_fk_organizacion,))
        query_string =  urlencode({'success_activate': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        #return redirect('listar_categoria_password')

    context = {
        'page' : 'Activar Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'categoria_password',
        'plural' : 'categoria_passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_categoria_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'item': itemObj
    }
    return render(request, 'panel/activar_objetos.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def desactivar_categoria_password(request, id, *args, **kwargs):
    '''Desactivar Password.'''
    
    itemObj = Password_Model.objects.get(id=id)

    if request.method == 'POST':
        itemObj.activo = '0'
        itemObj.deleted = datetime.datetime.now()

        #guardar historial        
        histObj = Accion_Model(
            accion = 'Desactivar Password',
            usuario = request.user,
            id_elemento = itemObj.id,
            nombre_elemento = itemObj.nombre,
            tipo_elemento = 'DEPARTAMENTO',
            tipo_accion = 'DESACTIVAR',
            descripcion = str('El Password [{}] {} fue desactivado.'.format(itemObj.id,itemObj.nombre)),
            created = datetime.datetime.now(),
            activo = '1'
        )
        histObj.save()

        itemObj.save()
        
        id_fk_organizacion = str(itemObj.fk_organizacion.id)
        print(f'id_fk_organizacion: {id_fk_organizacion}')
        base_url = reverse('ver_organizacion', args=(id_fk_organizacion,))
        query_string =  urlencode({'success_deactivate': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        #return redirect('listar_categoria_password')

    context = {
        'page' : 'Desactivar Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'categoria_password',
        'plural' : 'categoria_passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_categoria_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'item': itemObj
    }
    return render(request, 'panel/desactivar_objetos.html', context)


@login_required(login_url='entrar')
@allowed_users(allowed_roles=['admin'])
def eliminar_categoria_password(request, id, *args, **kwargs):
    '''Eliminar Password.'''
    
    itemObj = Password_Model.objects.get(id=id)
    
    if request.method == 'POST':

        #guardar historial 
        contenido_eliminado = [
            #campos genéricos
            ['id', itemObj.id],
            # ['activo', itemObj.activo],
            ['created', itemObj.created],
            ['updated', itemObj.updated],
            ['deleted', itemObj.deleted],
            #campos elemento
            ['nombre', itemObj.nombre],
            ['descripcion', itemObj.descripcion],
            ['fk_organizacion', itemObj.fk_organizacion],
            ['observaciones', itemObj.observaciones],
        ]
    
        histObj = Accion_Model(
            accion = 'Eliminar Password',
            usuario = request.user,
            id_elemento = itemObj.id,
            nombre_elemento = itemObj.nombre,
            tipo_elemento = 'DEPARTAMENTO',
            tipo_accion = 'ELIMINAR',
            descripcion = str('El Password [{}] {} fue eliminado.'.format(itemObj.id,itemObj.nombre)),
            contenido_eliminado = contenido_eliminado,
            created = datetime.datetime.now(),
            activo = '1'
        )
        histObj.save()

        itemObj.delete()
        
        id_fk_organizacion = str(itemObj.fk_organizacion.id)
        print(f'id_fk_organizacion: {id_fk_organizacion}')
        base_url = reverse('ver_organizacion', args=(id_fk_organizacion,))
        query_string =  urlencode({'success_delete': 'OK'})  
        url = '{}?{}'.format(base_url, query_string)  
        return redirect(url) 
        #return redirect('listar_categoria_password')

    context = {
        'page' : 'Eliminar Password',
        'icon' : 'bx bxs-user-rectangle',
        'color' : 'info',
        'singular' : 'categoria_password',
        'plural' : 'categoria_passwords',
        'parent': 'Passwords',
        'url_parent': 'listar_categoria_password',
        'info_contacto': info_header_contacto(request),
        'info_configuracion': info_configuracion(),
        'item': itemObj
    }
    return render(request, 'panel/eliminar_objetos.html', context)


