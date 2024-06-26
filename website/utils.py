# from panel.models import Persona_Model, Configuracion_Model
from website.models import Persona_Model

#=======================================================================================================================================
# Vista de inicio
#=======================================================================================================================================

def info_header_persona(request, *args, **kwargs):
    '''Entrega datos específicos del usuario, si existe'''
    if Persona_Model.objects.get(usuario=request.user.id):
        return Persona_Model.objects.get(usuario=request.user.id)
    else:
        return false

    # if request.user.groups.filter(name='admin').exists():
    #     return Persona_Model.objects.get(usuario=request.user.id)
    # elif request.user.groups.filter(name='agent').exists():
    #     return Persona_Model.objects.get(usuario=request.user.id)
    #return Persona_Model.objects.get(usuario=request.user.id)
    #return Persona_Model.objects.get(usuario=1)
    

def info_header_contacto(request, *args, **kwargs):
    '''Entrega datos específicos del usuario, si existe'''
    if request.user.groups.filter(name='admin').exists():
        return Contacto_Model.objects.get(usuario=request.user.id)
    elif request.user.groups.filter(name='soporte').exists():
        return Contacto_Model.objects.get(usuario=request.user.id)

