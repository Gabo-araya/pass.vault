from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse
from urllib.parse import urlencode
from django.db.models import Q
from django.template.defaultfilters import slugify

# Importar modelos desde apps de backend
# from panel.models import Ahora_Model, Servicio_Model, Proyecto_Model, Categoria_Proyecto_Model
# from panel.models import Actividad_Academica_Model, Actividad_Laboral_Model, Area_Interes_Model, Tecnologia_Model, Software_Model
# from panel.models import Pagina_Model, Articulo_Model, Categoria_Model, Etapa_Model
# from panel.models import Mensaje_Contacto_Model, Frontend_Search_Model, Backend_Search_Model, Configuracion_Model

# Importación de forms desde apps de backend
from website.forms import Mensaje_Contacto_Form, Frontend_Search_Form



from website.utils import info_header_persona


#=======================================================================================================================================
# Páginas del sitio
#=======================================================================================================================================

def inicio(request):
    '''Muestra una noticia destacada, acceso a blog y acceso a portafolio'''
    # page_content = Pagina_Model.objects.filter(nombre='inicio').filter(borrador=False)
    # proyecto_destacado = Proyecto_Model.objects.filter(borrador=False).filter(destacado=True).order_by('-created')[:1]
    # articulos = Articulo_Model.objects.filter(borrador=False).filter(destacado=False).order_by('-fecha')[:2]
    # articulo_destacado = Articulo_Model.objects.filter(borrador=False).filter(destacado=True).order_by('-fecha')[:1]
    # articulos_list = articulos[1:4]
    # articulo_destacado = articulos[:1]

    #print(f"proyecto_destacado: {proyecto_destacado}")
    #print(f"articulo_destacado: {articulo_destacado}")
    #print(f"articulos: {articulos}")
    #print(f"articulos_list: {articulos_list}")

    context = {
        'page' : 'Inicio',
        'info_persona': info_header_persona(request),
        #'info_configuracion': info_configuracion(),
        'url_actual': request.path,
        # 'page_content': "page_content",
        # 'proyecto_destacado': proyecto_destacado,
        # 'articulo_destacado': articulo_destacado,
        # 'articulos': articulos_list,
        # 'articulos': articulos,
    }

    return render(request, "website/index.html", context)



def blank(request):
    '''Muesta ejemplos de secciones'''
    # page_content = Pagina_Model.objects.filter(nombre='blank').filter(borrador=False)
    # articulos_list = Articulo_Model.objects.filter(borrador=False).order_by('-fecha')
    # actividades_academicas = Actividad_Academica_Model.objects.filter(borrador=False).filter(destacado=True).order_by('-fecha')
    context = {
        'page' : 'Blank',
        'info_persona': info_header_persona(request),
        #'info_configuracion': info_configuracion(),
        'url_actual': request.path,
        # 'page_content': page_content,
        # 'object_list': articulos_list,
        # 'actividades_academicas': actividades_academicas,
    }

    return render(request, "website/blank.html", context)




# def entrar(request):
#     '''Muesta ejemplo temporal de formulario'''

#     context = {
#         'page' : 'Entrar - Ejemplo de Form de contraseña',
#         'info_persona': info_header_persona(request),
#         'info_configuracion': info_configuracion(),
#         'url_actual': request.path,
#     }

#     return render(request, "website/blank.html", context)





#=======================================================================================================================================
# Blog
#=======================================================================================================================================


# def blog(request):
#     '''Muesta los artículos'''
#     page_content = Pagina_Model.objects.filter(nombre='blog').filter(borrador=False)
#     articulos_list = Articulo_Model.objects.filter(borrador=False).order_by('-fecha')
#     context = {
#         'page' : 'Blog',
#         'info_persona': info_header_persona(request),
#         'info_configuracion': info_configuracion(),
#         'page_content': page_content,
#         'object_list': articulos_list,
#     }

#     return render(request, "website/blog.html", context)



# def articulo(request, slug):
#     '''Muesta un artículo individual'''
#     # sólo se usa la primera parte del slug
#     url = slug.split(":")
#     id = url[0]
#     itemObj = Articulo_Model.objects.get(id=id)
#     context = {
#         'page' : 'Artículo',
#         'info_persona': info_header_persona(request),
#         'info_configuracion': info_configuracion(),
#         'item': itemObj,
#     }

#     return render(request, "website/articulo.html", context)



#=======================================================================================================================================
# Buscar
#=======================================================================================================================================

# def buscar(request, *args, **kwargs):
#     '''Muestra resultados de búsqueda.'''
#     page_content = Pagina_Model.objects.filter(nombre='buscar').filter(borrador=False)

#     form = Frontend_Search_Form()
#     vacio = True
#     termino_busqueda, resultado_articulos, resultado_proyectos, numero_articulos, numero_proyectos, total = '','','','','',''

#     if request.method == 'POST':
#         form = Frontend_Search_Form(request.POST)
#         #print(form)
#         if form.is_valid():
#             termino_busqueda = form.cleaned_data['nombre']
#             #print(termino_busqueda)
#             form.save()

#         if termino_busqueda == '':
#             vacio = True
#         else:
#             vacio = False

#             resultado_articulos = Articulo_Model.objects.distinct().filter(
#                 Q(nombre__icontains=termino_busqueda) |
#                 Q(resumen__icontains=termino_busqueda) |
#                 Q(contenido__icontains=termino_busqueda)
#                 ).filter(borrador=False).order_by('fecha')

#             resultado_proyectos = Proyecto_Model.objects.distinct().filter(
#                 Q(nombre__icontains=termino_busqueda) |
#                 Q(institucion__icontains=termino_busqueda) |
#                 Q(resumen__icontains=termino_busqueda) |
#                 Q(descripcion__icontains=termino_busqueda) |
#                 Q(desafios__icontains=termino_busqueda) |
#                 Q(aprendizajes__icontains=termino_busqueda) |
#                 Q(contenido__icontains=termino_busqueda)
#                 ).filter(borrador=False).order_by('fecha')

#             numero_articulos = resultado_articulos.count()
#             numero_proyectos = resultado_proyectos.count()
#             total = numero_articulos + numero_proyectos

#     context = {
#         'page': 'Resultados de búsqueda',
#         'termino_busqueda': termino_busqueda,
#         'vacio': vacio,
#         'resultado_articulos': resultado_articulos,
#         'resultado_proyectos': resultado_proyectos,
#         'numero_articulos': numero_articulos,
#         'numero_proyectos': numero_proyectos,
#         'total': total,
#         'info_persona': info_header_persona(request),
#         'info_configuracion': info_configuracion(),
#         'page_content': page_content,
#     }

#     return render(request, 'website/buscador.html', context)


#=======================================================================================================================================
# Contacto 
#=======================================================================================================================================

def contacto(request):
    '''Crear mensaje de contacto'''
    page_content = Pagina_Model.objects.filter(nombre='contacto').filter(borrador=False)

    form = Mensaje_Contacto_Form()
    error_message = ''
    success_message = ''
    if request.method == 'POST':
        form = Mensaje_Contacto_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info['nombre']
            email = info['email']
            asunto = info['asunto']
            mensaje = info['mensaje']

            mensaje_contacto = Mensaje_Contacto_Model(
                nombre = nombre,
                email = email,
                asunto = asunto,
                mensaje = mensaje,
            )

            mensaje_contacto.save()
            success_message = 'OK'
            #mensaje exitoso
            return redirect('gracias')

        else:
            #mensaje invalido
            #print("form invalido")
            error_message = 'ERROR'

    context = {
        'page' : 'Contacto',
        'info_persona': info_header_persona(request),
        #'info_configuracion': info_configuracion(),
        'url_actual': request.path,
        'page_content' : page_content,
        'success_message' : success_message,
        'error_message' : error_message,
    }
    return render(request, "website/contacto.html", context)


def gracias(request):
    '''Página de agradecimiento'''
    #page_content = Pagina_Model.objects.filter(nombre='gracias').filter(borrador=False)

    context = {
        'page' : 'Gracias',
        'info_persona': info_header_persona(request),
        #'info_configuracion': info_configuracion(),
        'url_actual': request.path,
        # 'page_content' : page_content,
    }
    return render(request, "website/gracias.html", context)

