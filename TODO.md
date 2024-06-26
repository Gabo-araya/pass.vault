# GENERADOR DE CONTRASEÑAS

## NAVEGACIÓN Y CARACTERISTICAS

- [] INICIO
    - [] Crear password aleatorio

- [] ENTRAR
    - [] Crear formulario de acceso a panel

- [] CONTACTO
    - [] Crear contenidos
    - [] Crear formulario contacto

- [] DASHBOARD
    - [] Mostrar bienvenida
        - Si el usuario no tiene creado "salt" (evaluar un solo uso)
        - Si el usuario no tiene passwords
        - Si el usuario no tiene categorías
    - [] Mostrar cantidad de categorías
    - [] Mostrar cantidad de passwords
    - [] Mostrar cantidad de las últimas 5 acciones realizadas

- [] CATEGORIAS
    - [] Listar categorías
    - [] Mostrar la categoría inicial "Sin Categoría"
    - [] Crear una categoría
    - [EVALUAR] Revisar detalle de categoría
    - [] Modificar una categoría
        - Cambiar nombre de categoría
        - Cambiar descripción
    - [] Eliminar una categoría con todos sus passwords
    - [] Eliminar una categoría y dejar todos sus passwords en la categoría inicial "Sin categoría"

- [] PASSWORDS
    - [] Listar passwords
    - [] Crear password aleatorio
        - [] Solamente si está creado "salt"
        - [] Botón guardar este password
        - [] Botón generar nuevo password
    - [] Crear password manual
        - [] Solamente si está creado "salt"
        - [] Opción para cambiar el password manual a formato L33t
    - [EVALUAR] Revisar detalle de password
    - [] Modificar un password
        - Cambiar password
        - Cambiar categoría
        - Cambiar URL
        - Cambiar descripción
    - [] Eliminar un password

- [] BUSCADOR
    - [] Listar categorías (vínculo a cada categoría)
    - [] Listar passwords (vínculo a revisar detalle de cada password)

- [] PERFIL
    - [] Agregar imagen de usuario
    - [] Cambiar nombre de usuario
    - [] Cambiar género de usuario
    - [] Agregar "salt" personalizado si el usuario no lo tiene instanciado
    - [EVALUAR] Modificar "salt" personalizado
        - Esto implica que todos los passwords guardados por este usuario deben ser modificados con el nuevo salt personalizado
    - [EVALUAR] Escoger tipo de encriptación 
        - Esto ddepende de la biblioteca secrets
    - [EVALUAR] Exportar passwords en CSV

- [] AYUDA
    - [] Crear contenidos e imágenes en html
    - [EVALUAR] Crear sistema de administración para tener distintas versiones de ayuda

- [] HISTORIAL
    - [] Listar acciones realizadas
    - [] Revisar detalle de acción realizada

- [] SALIR
    - [] Crear acción de salir



## TEMPLATES

- [] AGREGAR ARCHIVO TICKET
    - [] model
    - [] form
    - [] view
    - [] urls
    - [] registrar admin
    - [] mostrar en mensaje de ticket

- [] AGREGAR EVIDENCIA TICKET
    - [] model
    - [] form
    - [] view
    - [] urls
    - [] registrar admin
    - [] mostrar en mensaje de ticket

- [] CONTACTO: Agregar elementos relacionados
    - [] Mostrar tickets abiertos de informes en proceso
    - [] Mostrar mensajes creados y no enviados
    - [] Mostrar informes en proceso
    - [] Mostrar tareas de reunión
    - [] Mostrar tareas de proyectos
    - [] Mostrar capacitaciones realizadas

- [] ORGANIZACION: Agregar elementos relacionados
    - [] Mostrar Contactos
    - [] Mostrar Departamentos
    - [] Mostrar Proyectos
    - [] Mostrar Reuniones
    - [] Mostrar Capacitaciones
    - [] Mostrar Planes de soporte
    - [] Mostrar Contratos de soporte
    - [] Mostrar Informes de soporte
    - [] Mostrar Tickets

- [] CONFIGURACION: cambiar diseño completo
- [] VER PERFIL: cambiar diseño completo
- [] EDITAR PERFIL: cambiar diseño completo

- [] TIPO TICKET: Mostrar tickets
- [] TIPO SERVICIO TICKET: Mostrar tickets
- [] ESTADO_TICKET: Mostrar tickets
- [] TIPO INFORME SOPORTE: Mostrar informes

- [] INFORME SOPORTE PDF:
    - [x] Exportar a PDF
    - [] Agregar solicitante a ticket

- [] BUSCADOR GENERAL: 
    - [] Generar resultados de búsqueda por tipo de elemento


---

## VIEWS

- [] Revisar edición de configuración
- [] Agregar campos extra de modelos en tickets, contactos, organizaciones, planes, contratos, informes
- [] Revisar iconos de contexto views

## ESTRUCTURA

- [] Separar las listas de elementos en las vistas de detalle
- [] Separar la identificación de fichas de elementos
- [] Separar las templates

---



# Características Generador de contraseñas

Este generador de contraseñas utiliza la biblioteca secrets de python.
El salt personalizado que crea cada usuario desde su perfil se debe agregar al password.

- Funcionalidades
    - Acceso a la plataforma (Login)
    - Agregar/eliminar usuario
	    - Al eliminar el usuario se debe eliminar el perfil y viceversa.
	    - Al eliminar el usuario se debe eliminar todos los datos ingresados por ese usuario.
    - Editar perfil
	    - Imagen
	    - Género
	    - Agregar salt personalizado 
	    - Escoger tipo de encriptación (depende de la biblioteca secrets)
    - Manual de usuario (ayuda)
	    - Pasos iniciales
		    - Crear categorías
		    - Editar perfil y crear salt personalizado
	    - Cómo usar esta plataforma
		    - Crear una nueva categoría
		    - Modificar una categoría
		    - Eliminar una categoría
	    - Password
		    - Crear un nuevo password
		    - Modificar un password
		    - Eliminar un password
		- Perfil
			- Modificar perfil
			- Modificar imagen
			- Modificar salt personalizado
				- Esto implica que todos los passwords guardados por este usuario deben ser modificados con el nuevo salt personalizado
    - Funcionalidad de generación de password
		- Función de Listar passwords 
			- Lista máxima de 100 elementos
			- Se debe crear un filtro con datatables
		- Función de generar nuevo password 
			- Nombre sitio
			- Descripción
			- Categoría 
				- La categoría predeterminada debe ser "Sin categoría"
				- cada usuario puede agregar categorías personalizadas
			- Password aleatorio con características:
				- Cantidad caracteres
				- opción de incluir letras minúsculas de forma aleatoria
				- opción de incluir letras mayúsculas de forma aleatoria
				- opción de incluir números de forma aleatoria
				- opción de incluir caracteres especiales de forma aleatoria
				- FUNCION: Generar un nuevo password con las características escogidasy la cantidad de caracteres indicada
				- Botones
					- Me gusta este (función de guardar este password)
					- Quiero otro (recargar y generar un nuevo password)
			- Password personalizado con características:
				- Palabra o frase personalizada 
					- de forma obligatoria, cambiar los espacios por guión bajo
				- opción de cambiar frase en formato l33t
				- opción de incluir letras minúsculas de forma aleatoria
				- opción de incluir letras mayúsculas de forma aleatoria
				- opción de incluir números de forma aleatoria
				- opción de incluir caracteres especiales de forma aleatoria
				- FUNCION: 
					1. Sin opción l33t: Generar un nuevo password con las características escogidas, escogiendo aleatoriamente la mitad de los caracteres de la contraseña y cambiándolos con los caracteres indicados.
					2. Con opción l33t: Generar un nuevo password con las características escogidas, cambiar los espacios por guión bajo, modificando los caracteres para que asemejen a la escritura l33t.
				- Botones
					- Me gusta este (función de guardar este password)
					- Quiero otro (recargar y generar un nuevo password)
		- Función de eliminar pass
		- Función de eliminar categorías
			- Si se elimina una categoría, se deben eliminar todos los passwords en esa categoría
			- Incluir categoría predeterminada “Sin categoría”
		- Función de Buscador
		- Función de Historial
    



----


# Software instalado

## Instalar paquetes pip

- pip install Pillow
- pip install whitenoise
- pip install django-ckeditor



- pip3 freeze > requirements.txt


## Comandos Django

Activar env
    `source /home/gabo/django_proy/pass/env/bin/activate`

Crear superusuario
    `python3 manage.py createsuperuser`

Realizar migraciones
    `python3 manage.py makemigrations`
    `python3 manage.py migrate`

Obtener archivos estáticos
    `python3 manage.py collectstatic`

Iniciar el servidor
    `python3 manage.py runserver`






