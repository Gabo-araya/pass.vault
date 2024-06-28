from django.forms import ModelForm
from django import forms
from django.forms import ModelForm, Textarea, CheckboxInput
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Importación de modelos
from website.models import  Persona_Model, Categoria_Password_Model, Password_Model, Mensaje_Contacto_Model, Buscar_Password_Model
from website.models import Articulo_Model, Articulo_Categoria_Model, Articulo_Imagen_Model, Articulo_Archivo_Model, Accion_Model



#=======================================================================================================================================
# Forms
#=======================================================================================================================================
# - Persona_Form
# - Categoria_Password_Form
# - Password_Form
# - Mensaje_Contacto_Form
# - Buscar_Password_Form
# - Accion_Form
# - Articulo_Form
# - Articulo_Categoria_Form
# - Articulo_Imagen_Form
# - Articulo_Archivo_Form
# - Accion_Form




#=======================================================================================================================================
# EVALUAR Crear formulario de Bienvenida al crear nuevo usuario
#=======================================================================================================================================




#=======================================================================================================================================
# Persona_Form
#=======================================================================================================================================

class Persona_Form(ModelForm):

    class Meta:
        model = Persona_Model
        fields = [
            'primer_nombre',
            'otros_nombres',
            'apellido_paterno',
            'apellido_materno',
            'invertir_apellidos',
            # 'frase_salt',
            'fecha_nac',
            'imagen_perfil_usuario',
            'descripcion',
            # 'activo', #boolean #Este campo controla la papelera
        ]
    fecha_nac = forms.DateField(widget=AdminDateWidget(), required=False)
    # activo = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(Persona_Form, self).__init__(*args, **kwargs)
        
        self.fields['primer_nombre'].widget.attrs.update({'class':'form-control'})
        self.fields['otros_nombres'].widget.attrs.update({'class':'form-control'})
        self.fields['apellido_paterno'].widget.attrs.update({'class':'form-control'})
        self.fields['apellido_materno'].widget.attrs.update({'class':'form-control'})
        # self.fields['invertir_apellidos'].widget.attrs.update({'class':'form-control'})
        # frase_salt
        # fecha_nac
        self.fields['imagen_perfil_usuario'].widget.attrs.update({'class':'form-control-file'})
        self.fields['descripcion'].widget.attrs.update({'class':'form-control'})
        


#=======================================================================================================================================
# Categoria_Password_Form
#=======================================================================================================================================

class Categoria_Password_Form(ModelForm):

    class Meta:
        model = Categoria_Password_Model
        fields = [
            'nombre',
            # 'fk_usuario',
            'superior',
            'descripcion',
            # 'activo', #boolean #Este campo controla la papelera
        ]
    # fecha_nac = forms.DateField(widget=AdminDateWidget(), required=False)
    # activo = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(Persona_Form, self).__init__(*args, **kwargs)
        
        self.fields['nombre'].widget.attrs.update({'class':'form-control'})
        self.fields['superior'].widget.attrs.update({'class':'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class':'form-control'})
        
        

#=======================================================================================================================================
# Password_Form
#=======================================================================================================================================

class Password_Form(ModelForm):

    class Meta:
        model = Password_Model
        fields = [
            'nombre',
            'fk_usuario',
            'fk_categoría_password',
            'password',
            'password_email',
            'password_usuario',
            'url_login',

            'minusculas', #boolean
            'mayusculas', #boolean
            'numeros', #boolean
            'otros_caracteres', #boolean
            'formato_l33t', #boolean
            # 'aleatoria', #Este es un campo interno  #boolean

            'descripcion',
            'activo', #boolean #Este campo controla la papelera
        ]
    # fecha_nac = forms.DateField(widget=AdminDateWidget(), required=False)
    minusculas = forms.BooleanField(required=False)
    mayusculas = forms.BooleanField(required=False)
    numeros = forms.BooleanField(required=False)
    otros_caracteres = forms.BooleanField(required=False)
    formato_l33t = forms.BooleanField(required=False)
    # aleatoria = forms.BooleanField(required=False)
    activo = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(Persona_Form, self).__init__(*args, **kwargs)
        
        self.fields['nombre'].widget.attrs.update({'class':'form-control'})
        self.fields['usuario'].widget.attrs.update({'class':'form-control'})
        self.fields['fk_categoría_password'].widget.attrs.update({'class':'form-control'})
        self.fields['password'].widget.attrs.update({'class':'form-control'})
        self.fields['password_email'].widget.attrs.update({'class':'form-control'})
        self.fields['password_usuario'].widget.attrs.update({'class':'form-control'})
        self.fields['url_login'].widget.attrs.update({'class':'form-control'})

        self.fields['descripcion'].widget.attrs.update({'class':'form-control'})
        
        


#=======================================================================================================================================
# Mensaje_Contacto_Form
#=======================================================================================================================================

class Mensaje_Contacto_Form(ModelForm):
    class Meta:
        model = Mensaje_Contacto_Model
        fields = [
            'nombre',
            'email',
            'asunto',
            'mensaje',
        ]
        
    def __init__(self, *args, **kwargs):
        super(Mensaje_Contacto_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
            


#=======================================================================================================================================
# Buscar_Password_Form 
#=======================================================================================================================================

class Buscar_Password_Form(ModelForm):
    class Meta:
        model = Buscar_Password_Model
        fields = [
            'nombre',
            # 'fk_usuario',
        ]

    def __init__(self, *args, **kwargs):
        super(Buscar_Password_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



#=======================================================================================================================================
# Articulo_Form 
#=======================================================================================================================================

class Articulo_Form(ModelForm):

    class Meta:
        model = Articulo_Model
        fields = [
            'nombre',
            'slug',
            'fk_autor',
            'descripcion',
            'contenido',
            'imagen_lista',
            'imagen_grande',
            'fecha',
            
            'opt_tipo_articulo',
            'fk_articulo_categoria',
            
            'observaciones',
            'destacado', #boolean
            'activo', #boolean
        ]
        
    fecha = forms.DateField(widget=AdminDateWidget(), required=False)
    destacado = forms.BooleanField(required=False)
    activo = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(Articulo_Form, self).__init__(*args, **kwargs)
        
        self.fields['nombre'].widget.attrs.update({'class':'form-control'})
        self.fields['slug'].widget.attrs.update({'class':'form-control'})
        self.fields['autor'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen_lista'].widget.attrs.update({'class':'form-control-file'})
        self.fields['imagen_grande'].widget.attrs.update({'class':'form-control-file'})
        # fecha
        
        self.fields['opt_tipo_articulo'].widget.attrs.update({'class':'form-control'})
        self.fields['fk_articulo_categoria'].widget.attrs.update({'class':'form-control'})
        
        self.fields['observaciones'].widget.attrs.update({'class':'form-control'})
        # destacado
        # activo
        

#=======================================================================================================================================
# Articulo_Categoria_Form 
#=======================================================================================================================================

class Articulo_Categoria_Form(ModelForm):

    class Meta:
        model = Articulo_Categoria__Model
        fields = [
            'nombre',
            'slug',
            'descripcion',
            'icono',
            'color_icono',
            'imagen',
            
            'observaciones',
            'activo', #boolean
        ]
        
    activo = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(Articulo_Categoria_Form, self).__init__(*args, **kwargs)
        
        self.fields['nombre'].widget.attrs.update({'class':'form-control'})
        self.fields['slug'].widget.attrs.update({'class':'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class':'form-control'})
        self.fields['icono'].widget.attrs.update({'class':'form-control'})
        self.fields['color_icono'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen'].widget.attrs.update({'class':'form-control-file'})
        
        self.fields['observaciones'].widget.attrs.update({'class':'form-control'})
        
        
        

#=======================================================================================================================================
# Articulo_Imagen_Form 
#=======================================================================================================================================

class Articulo_Imagen_Form(ModelForm):

    class Meta:
        model = Articulo_Imagen_Model
        fields = [
            'nombre',
            'slug',
            'imagen',
            'descripcion',
            
            'observaciones',
            # 'activo', #boolean
        ]

    # activo = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(Articulo_Imagen_Form, self).__init__(*args, **kwargs)
        
        self.fields['nombre'].widget.attrs.update({'class':'form-control'})
        self.fields['slug'].widget.attrs.update({'class':'form-control'})
        self.fields['imagen'].widget.attrs.update({'class':'form-control-file'})
        self.fields['descripcion'].widget.attrs.update({'class':'form-control'})
        
        self.fields['observaciones'].widget.attrs.update({'class':'form-control'})

        
        

#=======================================================================================================================================
# Articulo_Archivo_Form 
#=======================================================================================================================================

class Articulo_Archivo_Form(ModelForm):

    class Meta:
        model = Articulo_Archivo_Model
        fields = [
            'nombre',
            'slug',
            'archivo',
            'descripcion',
            
            'observaciones',
            # 'activo', #boolean
        ]
        
    # activo = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(Articulo_Archivo_Form, self).__init__(*args, **kwargs)
        
        self.fields['nombre'].widget.attrs.update({'class':'form-control'})
        self.fields['slug'].widget.attrs.update({'class':'form-control'})
        self.fields['archivo'].widget.attrs.update({'class':'form-control-file'})
        self.fields['descripcion'].widget.attrs.update({'class':'form-control'})
        
        self.fields['observaciones'].widget.attrs.update({'class':'form-control'})

        
        

#=======================================================================================================================================
# Accion_Form
#=======================================================================================================================================

class Accion_Form(ModelForm):
    '''Especificacion de campos para form de accion (historial)'''
    class Meta:
        model = Accion_Model
        fields = [
            #'fk_usuario',
            'accion',
            
            'id_elemento',
            'nombre_elemento',
            'tipo_elemento',
            'tipo_accion',
            'descripcion',
            
            'contenido_inicial',
            'contenido_anterior',
            'contenido_actual',
            'contenido_eliminado',
            
            'activo'
        ]


    def __init__(self, *args, **kwargs):
        super(Accion_Form, self).__init__(*args, **kwargs)
        
        # self.fields['fk_usuario'].widget.attrs.update(
        #     {'class': 'custom-select', 'placeholder': ''})
        self.fields['accion'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})
        
        self.fields['id_elemento'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})
        self.fields['nombre_elemento'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})
        self.fields['tipo_elemento'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})
        self.fields['tipo_accion'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})
        self.fields['descripcion'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})

        self.fields['contenido_inicial'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})
        self.fields['contenido_anterior'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})
        self.fields['contenido_actual'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})
        self.fields['contenido_eliminado'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ''})
        # self.fields['activo'].widget.attrs.update(
        #     {'class': 'form-check-input', })


        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class':'form-control'})