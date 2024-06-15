from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.i18n import JavaScriptCatalog
import panel.views
import website.views


urlpatterns = [

# =======================================================================================================================================
# Login y funcionalidades
# =======================================================================================================================================

    # Login
    path('entrar/', panel.views.entrar, name='entrar'),
    path('salir/', panel.views.salir, name='salir'),

    # Dashboard
    path('', panel.views.app_panel_index, name='app_panel_index'),

    # Perfil
    # path('ver_perfil/', panel.views.ver_perfil, name='ver_perfil'),
    # path('editar_perfil/', panel.views.editar_perfil, name='editar_perfil'),

    # Configuración
    path('ver_configuracion/', panel.views.ver_configuracion, name='ver_configuracion'),
    path('editar_configuracion/', panel.views.editar_configuracion, name='editar_configuracion'),

    # Búsquedas
    path('resultados_busqueda/', panel.views.resultados_busqueda, name='resultados_busqueda'),

    #JS-Catalog para mostrar widget admin para fechas y horas
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),

# ======================================================================================================================================
# Elementos de Curriculum
# ======================================================================================================================================

    # Personas
    # path('personas/', panel.views.listar_personas, name='listar_personas'),
    # path('personas/<int:id>/', panel.views.ver_persona, name='ver_persona'),
    # path('personas/crear/', panel.views.crear_persona, name='crear_persona'),
    # path('persona/modificar/<int:id>/', panel.views.modificar_persona, name='modificar_persona'),
    # path('persona/eliminar/<int:id>/', panel.views.eliminar_persona, name='eliminar_persona'),


    # Passwords
    path('passwords/', panel.views.listar_passwords, name='listar_passwords'),
    path('passwords/<int:id>/', panel.views.ver_password, name='ver_password'),
    path('passwords/crear/', panel.views.crear_password, name='crear_password'),
    path('passwords/modificar/<int:id>/', panel.views.modificar_password, name='modificar_password'),
    path('passwords/eliminar/<int:id>/', panel.views.eliminar_password, name='eliminar_password'),

    # Categorías de password
    path('categorias_password/', panel.views.listar_categorias_password, name='listar_categorias_password'),
    path('categorias_password/<int:id>/', panel.views.ver_categoria_password, name='ver_categoria_password'),
    path('categorias_password/crear/', panel.views.crear_categoria_password, name='crear_categoria_password'),
    path('categorias_password/modificar/<int:id>/', panel.views.modificar_categoria_password, name='modificar_categoria_password'),
    path('categorias_password/eliminar/<int:id>/', panel.views.eliminar_categoria_password, name='eliminar_categoria_password'),

    # Archivos
    # path('archivos/', panel.views.listar_archivos, name='listar_archivos'),
    # path('archivos/<int:id>/', panel.views.ver_archivo, name='ver_archivo'),
    # path('archivos/crear/', panel.views.crear_archivo, name='crear_archivo'),
    # path('archivos/modificar/<int:id>/', panel.views.modificar_archivo, name='modificar_archivo'),
    # path('archivos/eliminar/<int:id>/', panel.views.eliminar_archivo, name='eliminar_archivo'),


# ======================================================================================================================================
# Elementos de Sitio web
# ======================================================================================================================================

    # Páginas
    # path('paginas/', panel.views.listar_paginas, name='listar_paginas'),
    # path('paginas/<int:id>/', panel.views.ver_pagina, name='ver_pagina'),
    # path('paginas/crear/', panel.views.crear_pagina, name='crear_pagina'),
    # path('paginas/modificar/<int:id>/', panel.views.modificar_pagina, name='modificar_pagina'),
    # path('paginas/eliminar/<int:id>/', panel.views.eliminar_pagina, name='eliminar_pagina'),

    # Artículos
    # path('articulos/', panel.views.listar_articulos, name='listar_articulos'),
    # path('articulos/<int:id>/', panel.views.ver_articulo, name='ver_articulo'),
    # path('articulos/crear/', panel.views.crear_articulo, name='crear_articulo'),
    # path('articulos/modificar/<int:id>/', panel.views.modificar_articulo, name='modificar_articulo'),
    # path('articulos/eliminar/<int:id>/', panel.views.eliminar_articulo, name='eliminar_articulo'),

    # Categorías
    # path('categorias_articulo/', panel.views.listar_categorias, name='listar_categorias'),
    # path('categorias_articulo/<int:id>/', panel.views.ver_categoria, name='ver_categoria'),
    # path('categorias_articulo/crear/', panel.views.crear_categoria, name='crear_categoria'),
    # path('categorias_articulo/modificar/<int:id>/', panel.views.modificar_categoria, name='modificar_categoria'),
    # path('categorias_articulo/eliminar/<int:id>/', panel.views.eliminar_categoria, name='eliminar_categoria'),

    # Etapas
    # path('etapas/', panel.views.listar_etapas, name='listar_etapas'),
    # path('etapas/<int:id>/', panel.views.ver_etapa, name='ver_etapa'),
    # path('etapas/crear/', panel.views.crear_etapa, name='crear_etapa'),
    # path('etapas/modificar/<int:id>/', panel.views.modificar_etapa, name='modificar_etapa'),
    # path('etapas/eliminar/<int:id>/', panel.views.eliminar_etapa, name='eliminar_etapa'),

    # Imágenes
    # path('imagenes/', panel.views.listar_imagenes, name='listar_imagenes'),
    # path('imagenes/<int:id>/', panel.views.ver_imagen, name='ver_imagen'),
    # path('imagenes/crear/', panel.views.crear_imagen, name='crear_imagen'),
    # path('imagenes/modificar/<int:id>/', panel.views.modificar_imagen, name='modificar_imagen'),
    # path('imagenes/eliminar/<int:id>/', panel.views.eliminar_imagen, name='eliminar_imagen'),

    # Mensajes de contacto
    # path('mensajes_contacto/', panel.views.listar_mensajes_contacto, name='listar_mensajes_contacto'),
    # path('mensajes_contacto/<int:id>/', panel.views.ver_mensaje_contacto, name='ver_mensaje_contacto'),
    # path('mensajes_contacto/eliminar/<int:id>', panel.views.eliminar_mensaje_contacto, name='eliminar_mensaje_contacto'),


# ======================================================================================================================================
# Reset de Password
# ======================================================================================================================================

    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name='login/password_reset.html'),
    #     name='reset_password'),
    # path('reset_password_enviado/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_sent.html'),
    #     name='password_reset_done'),
    # path('reset_password_confirmado/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_form.html'),
    #     name='password_reset_confirm'),
    # path('reset_password_completado/', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_done.html'),
    #     name='password_reset_complete'),


# ======================================================================================================================================
# Otras rutas
# ======================================================================================================================================

    # path('blank/', panel.views.blank, name='blank'),
    # path('ayuda/', panel.views.ayuda, name='ayuda'),
    path('test/', panel.views.test, name='test'),

] # fin urlpatterns