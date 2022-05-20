from django.utils.timezone import now
from Online_Store.config import LOGO_SISTEMA, NOMBRE_SISTEMA, NOMBRE_AUTOR, NOMBRE_INSTITUCION
from Seguridad.models import ModuloGrupo

def addUserData(request, data):
    data['hoy'] = now
    data['usuario'] = request.user
    data['logo'] = LOGO_SISTEMA
    data['sistema'] = NOMBRE_SISTEMA
    data['institucion'] = NOMBRE_INSTITUCION
    data['autor'] = NOMBRE_AUTOR
    data['grupos'] = ModuloGrupo.objects.filter(grupos__in=request.user.groups.all()).order_by('prioridad')
    #data['foto']=Empleado.objects.get(user=request.user)
    data['grupo'] = request.user.groups.all()[0]


