from django.shortcuts import render
from .models import Persona
from django.contrib.auth import get_user_model
# Create your views here.

def login(request):
    try:
        usuario=get_user_model()
        #Persona.objects.get_or_create(cedula=31456,primer_nombre="Jesus",primer_apellido="Marin")
        persona=Persona.objects.get(id_persona=1)
        #usuario.objects.create_superuser(username="ale14",id_persona=persona,password="141204.j")
        #Mostrando datos del usuario desde su modelo
        usuario=usuario.objects.get(id_persona=1)
        print("DESDE EL HIJO ACCEDIENDO A DATOS DEL PADRE")
        print(usuario.id_persona.primer_nombre)
        print(f"{usuario.id_persona.cedula}\n")
        #Mostrandolo desde su padre
        print("ACCEDIENDO DESDE EL PADRE A LOS DATOS DEL HIJO USUARIO")
        print(persona.dato_usuario.username)
        context={}
        return render(request,'login.html',context)
    except Exception as e :
        print(f"Error{e}")  