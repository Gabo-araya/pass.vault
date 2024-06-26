from django.forms import ModelForm
from django import forms
from django.forms import ModelForm, Textarea, CheckboxInput
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Importación de modelos
from website.models import Backend_Search_Model, Mensaje_Contacto_Model



#=======================================================================================================================================
# Mensaje_Contacto
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
# Frontend_Search 
#=======================================================================================================================================

class Buscar_Password_Form(ModelForm):
    class Meta:
        model = Buscar_Password_Model
        fields = [
            'nombre',
        ]

    def __init__(self, *args, **kwargs):
        super(Buscar_Password_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



            
#=======================================================================================================================================
# Frontend_Search 
#=======================================================================================================================================

class Frontend_Search_Form(ModelForm):
    class Meta:
        model = Frontend_Search_Model
        fields = [
            'nombre',
        ]

    def __init__(self, *args, **kwargs):
        super(Frontend_Search_Form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

