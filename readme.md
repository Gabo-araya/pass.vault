# Proyecto de Administrador de contraseñas

_Administración de contraseñas_

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.


## Pre-requisitos 📋

_Esta es una lista de los paquetes que deben estar instalados previamente:_

* Python 3
	- Lenguaje de programación
	- [Ayuda - https://docs.microsoft.com/en-us/windows/python/beginners)](https://docs.microsoft.com/en-us/windows/python/beginners)
	- [Curso Django desde Cero en youtube](https://www.youtube.com/watch?v=vo4VF3neyrs)

* Pip
	- Gestor de instalación de paquetes PIP
	- [Ayuda - https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/](https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/)

* Virtualenv
	- Creador de entornos virtuales para Python
	- [Ayuda - https://techexpert.tips/es/windows-es/instalacion-del-entorno-virtual-de-python-en-windows/](https://techexpert.tips/es/windows-es/instalacion-del-entorno-virtual-de-python-en-windows/)
	- [Ayuda - https://atareao.es/como/entorno-virtual-en-python-como-y-para-que/](https://atareao.es/como/entorno-virtual-en-python-como-y-para-que/)


## Instalación pre-requisitos - Windows 🔧

Muchas veces tenemos ese problema común de no poder instalar ciertas librerías o realizar configuraciones para poder desarrollar en Windows para Web y es por ello que en éste tutorial vamos a ver los pasos para instalar Python y configurarlo con Pip y Virtualenv para así poder empezar a desarrollar aplicaciones basadas en éste lenguaje e instalar Django para crear aplicaciones web. [Ver video -> **https://www.youtube.com/watch?v=sG7Q-r_SZhA**](https://www.youtube.com/watch?v=sG7Q-r_SZhA)

1. Descargamos e instalamos Python 3.6 (o una versión superior) para Windows
	- [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Agregaremos Python a las variables de entorno de nuestro sistema si es que no se agregaron durante la instalación para que así podamos ejecutarlo desde la terminal `/cmd`
	- `C:\Python34 y C:\Python34\Scripts`

3. Ejecutamos Pip para verificar que esté instalado correctamente
	- `pip --version`

4. Instalamos Virtualenv con pip
	- `pip install virtualenv`

5. Verificamos la versión de Virtualenv
	- `virtualenv --version`

6. Crearemos un entorno virtual con Python
	- `virtualenv test`

7. Iniciamos el entorno virtual
	- `.\test\Scripts\activate`

8. Finalmente desactivamos el entorno virtual
	- `deactivate`


## Instalación pre-requisitos - GNU/Linux 🔧

1. Ejecutamos Pip para verificar que esté instalado correctamente
	- `pip3 --version`

2. Instalamos Virtualenv con pip
	- `pip3 install virtualenv`

3. Verificamos la versión de Virtualenv
	- `virtualenv --version`

4. Crearemos un entorno virtual con Python
	- `python3 -m venv /home/gabo/envs/gaboaraya/env`

5. Activamos el entorno virtual
	- `source /home/gabo/envs/gaboaraya/env/bin/activate`

6. Finalmente desactivamos el entorno virtual
	- `deactivate`


## Instalación Local 🚀

Seguir los siguientes pasos para la instalación local.

1. Clonar el repositorio o subir/descargar los archivos.

	- `git clone https://github.com/Gabo-araya/pass`

2. Instalar los requerimientos.

	- `python3 -m pip install -r requirements.txt`

3. Revisar settings.py y .env
	- Revisar que la sección de base de datos esté configurada para que trabaje con la base de datos SQLite en local.

3. Realizar migraciones
	- Crear archivos de migración: `python3 manage.py makemigrations`
	- Realizar migraciones`python3 manage.py migrate`

4. Crear superusuario
	- `python3 manage.py createsuperuser`
	- Si se usa Cpanel es necesario indicar el encoding primero vía terminal: 
		-`export PYTHONIOENCODING="UTF-8"; python3.6 manage.py createsuperuser`

5. Obtener archivos estáticos
	- `python3 manage.py collectstatic`

6. Iniciar el servidor
	- `python3 manage.py runserver`
	- Iniciar en un puerto específico (:8000):`python3 manage.py runserver 8000`


## Funcionalidades 

### Funcionalidades del Sitio Web
URL de acceso: [http://localhost:8000/](http://localhost:8000/)

1. Sección **INICIO**
	- Muestra opción para crear un password aleatorio con cierta cantidad de caracteres.

2. Sección **ENTRAR**
	- Muestra el formulario de login para acceder al panel de administración

3. Sección **CONTACTO**
	- Muestra el contenido de la página y el formulario de contacto.



### Funcionalidades del Panel de Administración 
URL de acceso: [http://localhost:8000/panel/](http://localhost:8000/panel/)

1. Sección **DASHBOARD**
	- Muestra las opciones que ofrece el sistema (cantidad de categorías, cantidad de passwords, las últimas 5 acciones realizadas, etc.)

2. Sección **CATEGORÍAS**
	- Muestra una lista con las categorías disponibles. 
	- Existe una categoría "Sin categoría" de forma predeterminada
	- Se pueden realizar acciones de creación, ver detalle, modificación, eliminación.

3. Sección **PASSWORDS**
	- Muestra una lista con los passwords creados. 
	- Se pueden realizar acciones de creación, ver detalle, modificación, eliminación.
	- Se puede ingresar un nuevo password generado aleatoriamente o uno nuevo manualmente.
	- Se puede agregar el password en una categoría
	- Se puede agregar una descripción y una URL del lugar donde debe ir el password

4. Sección **BUSCADOR**
	- Permite encontrar un password
	- Se pueden realizar acciones ver detalle.

5. Sección **PERFIL**
	- Permite editar las características del perfil.
		- Imagen del usuario
		- Nombre del usuario
		- Género del usuario
	- Permite modificar otras configuraciones (opcional)
		- Agregar "salt" personalizado 
			- Esto implica que todos los passwords guardados por este usuario deben ser modificados con el nuevo salt personalizado
	    	- Escoger tipo de encriptación (depende de la biblioteca secrets)

6. Sección **AYUDA**
	- Manual de usuario (ayuda)
	    - Pasos iniciales
		    - Crear categorías
		    - Editar perfil y crear salt personalizado
	    - Cómo usar esta plataforma
		    - Crear una nueva categoría
		    - Modificar una categoría
		    - Eliminar una categoría (se eliminan todos los passwords de esa categoría)
	    - Password
		    - Crear un nuevo password
		    - Eliminar un password
		- Perfil
			- Modificar perfil (nombre, género e imagen)
			- Modificar salt personalizado (Esto implica que todos los passwords guardados por este usuario deben ser modificados con el nuevo salt personalizado)

7. Sección **HISTORIAL**
	- Muestra una lista con la descripción de las acciones realizadas en el sistema. 

8. Sección **SALIR**
	- Permite cerrar la sesión y salir del panel de administración.



## Datos de usuarios 📦

### Usuarios panel de control
URL de acceso: [http://localhost:8000/panel/](http://localhost:8000/panel/)
- Usuario: `gabo`
	- Password: `user.123456`
	
### Acceso a sección de administración de Django
URL de acceso: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- Usuario: `admin`
	- Password: `admin.123456`
- Usuario: `gabo`
	- Password: `user.123456`


## Herramientas de construcción 🛠️

_Estas son las herramientas que hemos utilizado en nuestro proyecto_

* [Django](https://www.djangoproject.com/) - El framework web usado


## Autores ✒️

* **[Gabo Araya](https://github.com/Gabo-araya/)** - *Sitio web, panel de administración y documentación*



