from django.db import models

# Create your models here.


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
# Table `Contacto_Model`
#=======================================================================================================================================


class Persona_Model(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Usuario') # user
    nombre = models.CharField(max_length=250, verbose_name='Nombre [*]')
    slug = models.SlugField(null=True, blank=True, unique=True, verbose_name='Slug')
    primer_nombre = models.CharField(max_length=100, verbose_name='Primer nombre [*]')
    otros_nombres = models.CharField(max_length=100, null=True, blank=True, verbose_name='Otros nombres')
    apellido_paterno = models.CharField(max_length=50, verbose_name='Apellido paterno [*]')
    apellido_materno = models.CharField(max_length=50, verbose_name='Apellido materno [*]')
    invertir_apellidos = models.BooleanField(default=False, blank=True, verbose_name='Invertir apellidos', help_text='Esta opción permite poner el apellido materno antes del apellido paterno.')

    fecha_nac = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento', help_text='Fecha de nacimiento.')
    rut = models.CharField(max_length=12, verbose_name='Rut [*]', help_text='Rut con dígito verificador - Formato: 12345678-9')
    titulo = models.CharField(max_length=250, verbose_name='Titulo personal [*]')
    mini_bio = RichTextField(verbose_name='Mini biografía [*]')
    biografia = RichTextField(null=True, blank=True, verbose_name='Biografía')
    perfil_academico = RichTextField(null=True, blank=True, verbose_name='Perfil académico')
    perfil_profesional = RichTextField(null=True, blank=True, verbose_name='Perfil profesional')
    nacionalidad = models.CharField(max_length=50, verbose_name='Nacionalidad [*]', help_text='')
    ciudad_nac = models.CharField(max_length=50, verbose_name='Ciudad de nacimiento [*]', help_text='')
    archivo = models.FileField(null=True, blank=True, upload_to='archivos/', default='', verbose_name='CV en PDF [*]')

    fk_area_interes = models.ManyToManyField('Area_Interes_Model', blank=True, verbose_name='Área de Interés [*]') 
    fk_tecnologias = models.ManyToManyField('Tecnologia_Model', blank=True, verbose_name='Tecnología [*]') 
    fk_software = models.ManyToManyField('Software_Model', blank=True, verbose_name='Software [*]') 

    telefono_movil = models.CharField(max_length=50, verbose_name='Teléfono móvil [*]', help_text='')
    email = models.EmailField(max_length=250, verbose_name='Email [*]', help_text='')

    url_github = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL GitHub', help_text='Dirección del perfil de GitHub')
    url_facebook = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL Facebook', help_text='Dirección del perfil de Facebook')
    url_youtube = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL Youtube', help_text='Dirección del perfil de Youtube')
    url_linkedin = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL Linkedin', help_text='Dirección del perfil de Linkedin')
    url_twitter = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL Twitter', help_text='Dirección del perfil de Twitter')
    url_instagram = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL Instagram', help_text='Dirección del perfil de Instagram')

    class Meta:
        ''' Define el nombre singular y plural, y el ordenamiento de los elementos. '''
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['id']
        
    def save(self, *args, **kwargs):
        '''Modifica el método save para agregar el slug de forma automática'''
        
        if self.slug is None:
            # self.slug = slugify(self.nombre)
            self.slug = (f"{self.id}:{slugify(self.nombre)}")
            
        super().save(*args, **kwargs)

    def __str__(self):
        if self.invertir_apellidos == True:
            return str('{} {} {}'. format(self.primer_nombre, self.apellido_materno, self.apellido_paterno))
        else: 
            return str('{} {} {}'. format(self.primer_nombre, self.apellido_paterno, self.apellido_materno))


