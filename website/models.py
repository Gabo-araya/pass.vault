from django.db import models


class Campos_Genericos(models.Model):
    ''' Clase abstracta que agrega campos que deben estar presentes en todos los modelos de esta app.     '''

    descripcion = models.TextField(null=True, blank=True, default="Sin descripción.", verbose_name='Descripción')
    activo = models.BooleanField(null=True, blank=True, default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Fecha de última modificación')
    deleted = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de desactivación')

    class Meta: 
        abstract = True



#=======================================================================================================================================
# Tablas 
#=======================================================================================================================================
# - Persona_Model
# - Categoria_Password_Model
# - Password_Model
# - Mensaje_Contacto_Model
# - Buscar_Password_Model
# - Accion_Model
# - Articulo_Model
# - Articulo_Categoria_Model
# - Articulo_Imagen_Model
# - Articulo_Archivo_Model
# - Accion_Model

#=======================================================================================================================================


#=======================================================================================================================================
# Persona_Model
#=======================================================================================================================================


class Persona_Model(Campos_Genericos):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Usuario') # user
    # nombre = models.CharField(max_length=250, verbose_name='Nombre [*]')
    # slug = models.SlugField(null=True, blank=True, unique=True, verbose_name='Slug')
    primer_nombre = models.CharField(max_length=100, verbose_name='Primer nombre [*]')
    otros_nombres = models.CharField(max_length=100, null=True, blank=True, verbose_name='Otros nombres')
    apellido_paterno = models.CharField(max_length=50, verbose_name='Apellido paterno [*]')
    apellido_materno = models.CharField(max_length=50, verbose_name='Apellido materno [*]')
    invertir_apellidos = models.BooleanField(default=False, blank=True, verbose_name='Invertir apellidos', help_text='Esta opción permite poner el apellido materno antes del apellido paterno.')
    frase_salt = models.SlugField(null=True, blank=True, unique=True, verbose_name='Frase Salt')

    # fecha_nac = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento', help_text='Fecha de nacimiento.')
    # rut = models.CharField(max_length=12, verbose_name='Rut [*]', help_text='Rut con dígito verificador - Formato: 12345678-9')
    # titulo = models.CharField(max_length=250, verbose_name='Titulo personal [*]')
    # mini_bio = RichTextField(verbose_name='Mini biografía [*]')
    # biografia = RichTextField(null=True, blank=True, verbose_name='Biografía')
    # perfil_academico = RichTextField(null=True, blank=True, verbose_name='Perfil académico')
    # perfil_profesional = RichTextField(null=True, blank=True, verbose_name='Perfil profesional')
    # nacionalidad = models.CharField(max_length=50, verbose_name='Nacionalidad [*]', help_text='')
    # ciudad_nac = models.CharField(max_length=50, verbose_name='Ciudad de nacimiento [*]', help_text='')

    imagen_perfil_usuario = models.ImageField(null=True, blank=True, upload_to='imagen_perfil_usuario/', default='', verbose_name='Imagen del perfil del usuario')

    # fk_area_interes = models.ManyToManyField('Area_Interes_Model', blank=True, verbose_name='Área de Interés [*]') 
    # fk_tecnologias = models.ManyToManyField('Tecnologia_Model', blank=True, verbose_name='Tecnología [*]') 
    # fk_software = models.ManyToManyField('Software_Model', blank=True, verbose_name='Software [*]') 

    # telefono_movil = models.CharField(max_length=50, verbose_name='Teléfono móvil [*]', help_text='')
    # email = models.EmailField(max_length=250, verbose_name='Email [*]', help_text='')

    # url_github = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL GitHub', help_text='Dirección del perfil de GitHub')
    # url_facebook = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL Facebook', help_text='Dirección del perfil de Facebook')
    # url_youtube = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL Youtube', help_text='Dirección del perfil de Youtube')
    # url_linkedin = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL Linkedin', help_text='Dirección del perfil de Linkedin')
    # url_twitter = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL Twitter', help_text='Dirección del perfil de Twitter')
    # url_instagram = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL Instagram', help_text='Dirección del perfil de Instagram')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['id']
        
    # def save(self, *args, **kwargs):
    #     '''Modifica el método save para agregar el slug de forma automática'''
        
    #     if self.slug is None:
    #         # self.slug = slugify(self.nombre)
    #         self.slug = (f"{self.id}:{slugify(self.nombre)}")
            
    #     super().save(*args, **kwargs)

    def __str__(self):
        if self.invertir_apellidos == True:
            return str('{} {} {}'. format(self.primer_nombre, self.apellido_materno, self.apellido_paterno))
        else: 
            return str('{} {} {}'. format(self.primer_nombre, self.apellido_paterno, self.apellido_materno))





#=======================================================================================================================================
# Categoria_Password_Model
#=======================================================================================================================================

class Categoria_Password_Model(Campos_Genericos):
    ''' Clase para categorias de Passwords. '''
    nombre = models.CharField(max_length=250, verbose_name='Categoría de Password [*]')
    superior = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="subcategorias", verbose_name="Categoría Superior")
    
    class Meta:
        verbose_name = 'Categoría de Password'
        verbose_name_plural = 'Categorías de Password'
        ordering = ['id']

    def nombre_modelo(self):
        ''' Retorna un string que será el nombre que mostrará el objeto.'''
        return str('{}'. format(self.nombre))

    def __str__(self):
        ''' Retorna un string con el nombre del objeto en las listas y en el admin. '''
        return self.nombre_modelo()
    




#=======================================================================================================================================
# Password_Model
#=======================================================================================================================================

class Password_Model(Campos_Genericos):
    ''' Clase para Passwords. '''
    nombre = models.CharField(max_length=250, verbose_name='Nombre del Sitio o Servicio [*]')
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Usuario') # user
    fk_categoria_password = models.ForeignKey(Categoria_Password_Model, on_delete=models.DO_NOTHING, related_name="fk_categoria_password", verbose_name='Categoría [*]') 
    password = models.CharField(max_length=250, verbose_name='Password [*]')
    password_email = models.CharField(max_length=250, null=True, blank=True, verbose_name='Email asociado al password')
    password_usuario = models.CharField(max_length=250, null=True, blank=True, verbose_name='Usuario asociado al password')
    url = models.CharField(max_length=250, null=True, blank=True, verbose_name='URL')

    minusculas = models.BooleanField(null=True, blank=True, default=True, verbose_name='Minúsculas')
    mayusculas = models.BooleanField(null=True, blank=True, default=True, verbose_name='Mayúsculas')
    numeros = models.BooleanField(null=True, blank=True, default=True, verbose_name='Números')
    otros_caracteres = models.BooleanField(null=True, blank=True, default=True, verbose_name='Otros Caracteres')
    formato_l33t = models.BooleanField(null=True, blank=True, default=True, verbose_name='Formato L33t')
    aleatoria = models.BooleanField(null=True, blank=True, default=True, verbose_name='Aleatoria')

    
    class Meta:
        verbose_name = 'Password'
        verbose_name_plural = 'Password'
        ordering = ['id']

    def nombre_modelo(self):
        ''' Retorna un string que será el nombre que mostrará el objeto.'''
        return str('{}'. format(self.nombre))

    def __str__(self):
        ''' Retorna un string con el nombre del objeto en las listas y en el admin. '''
        return self.nombre_modelo()
    




#=======================================================================================================================================
# Mensaje_Contacto_Model
#=======================================================================================================================================

class Mensaje_Contacto_Model(models.Model):
    ''' Guarda los mensajes del formulario de contacto. '''
    nombre = models.CharField(max_length=250, verbose_name='Nombre [*]')
    email = models.EmailField(max_length=250, verbose_name='Email [*]')
    asunto = models.CharField(max_length=250, verbose_name='Asunto [*]')
    mensaje = models.TextField(verbose_name='Mensaje [*]')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Mensaje Formulario Contacto'
        verbose_name_plural = 'Mensajes Formulario Contacto'
        ordering = ['-created']

    def __str__(self):
        return self.asunto



#=======================================================================================================================================
# Buscar_Password_Model
#=======================================================================================================================================

class Buscar_Password_Model(Campos_Genericos):
    ''' Guarda las búsquedas de passwords. '''
    nombre = models.CharField(max_length=250, verbose_name='Término de búsqueda [*]')
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Usuario') # user
    # created  = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Fecha de creación')
        
    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Búsqueda de passwords'
        verbose_name_plural = 'Búsquedas de passwords'
        ordering = ['-created']

    def __str__(self):
        return self.nombre
    




#=======================================================================================================================================
# Accion_Model
#=======================================================================================================================================

class Accion_Model(Campos_Genericos):
    '''Guarda información de las acciones realizadas por un usuario.'''
    
    TIPO_ACCION_HISTORIAL_CHOICES = (
        ('CREAR', 'Crear'), 
        ('MODIFICAR', 'Modificar'), 
        ('ACTIVAR', 'Activar' ),
        ('DESACTIVAR', 'Desactivar'), 
        ('ELIMINAR', 'Eliminar'), 
    )
    
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Usuario') 
    accion = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Acción')

    id_elemento = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='ID')
    nombre_elemento = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Nombre')
    tipo_elemento = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name='Tipo de Elemento')
    tipo_accion = models.CharField(max_length=20, choices=TIPO_ACCION_HISTORIAL_CHOICES, verbose_name='Tipo de Acción [*]')
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name='Descripción')

    contenido_inicial = models.TextField(null=True, blank=True, verbose_name='Contenido inicial') #array con el contenido del elemento 
    contenido_anterior = models.TextField(null=True, blank=True, verbose_name='Contenido anterior') #array con el contenido del elemento
    contenido_actual = models.TextField(null=True, blank=True, verbose_name='Contenido actual') #array con el contenido del elemento 
    contenido_eliminado = models.TextField(null=True, blank=True, verbose_name='Contenido eliminado') #array con el contenido del elemento

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos.'''
        verbose_name = 'Acción'
        verbose_name_plural = 'Acciones'
        ordering = ['-id']

    def nombre_modelo(self):
        '''Retorna un string que será el nombre que mostrará el objeto.'''
        return str('{} - {} - {}'. format(self.tipo_accion, self.tipo_elemento, self.usuario))

    def __str__(self):
        ''' Retorna un string con el nombre del objeto en las listas y en el admin.'''
        return self.nombre_modelo()







