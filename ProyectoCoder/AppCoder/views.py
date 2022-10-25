from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import CursoFormulario, ProfesorFormulario
from .models import Curso, Profesor

# Create your views here.


def inicio(request):
    
    return render(request, "inicio.html")

# def cursos(request):

#     return render(request, "cursos.html")

# def profesores(request):
    
#     return render(request, "profesores.html")

def estudiantes(request):
    
    return render(request, "estudiantes.html")

def entregables(request):
    
    return render(request, "entregables.html")

def cursos(request):
    
    if request.method == 'POST':
        
        miFormulario = CursoFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            curso = Curso (nombre=informacion["curso"], camada=informacion["camada"])
            
            curso.save()
            
            return render(request, "inicio.html")
    
    else:
        
        miFormulario = CursoFormulario()
    
    return render(request, "cursos.html", {"miFormulario":miFormulario})

def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "profesores.html", {"miFormulario":miFormulario})

def buscar(request):
    
    if request.GET["camada"]:
        
        # respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        
        return render(request, "inicio.html", {"cursos":cursos, "camada":camada})
    
    else:
        
        respuesta = "No enviaste datos"

    # return HttpResponse(respuesta)
    return render(request, "inicio.html", {"respuesta":respuesta})
        