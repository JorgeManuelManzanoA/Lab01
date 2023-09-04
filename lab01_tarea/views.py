from django.shortcuts import render
from .models import Lab01_tarea

def sumar(request, num1, num2):
    resultado = int(num1) + int(num2)
    operacion = Lab01_tarea(num1=num1, num2=num2, tipo_operacion="Suma", resultado=resultado)
    operacion.save()
    return render(request, 'lab01_tarea/vista.html', {'mensaje': f"La suma de {num1} + {num2} = {resultado}"})

def restar(request, num1, num2):
    resultado = int(num1) - int(num2)
    operacion = Lab01_tarea(num1=num1, num2=num2, tipo_operacion="Resta", resultado=resultado)
    operacion.save()
    return render(request, 'lab01_tarea/vista.html', {'mensaje': f"La resta de {num1} - {num2} = {resultado}"})

def multiplicar(request, num1, num2):
    resultado = int(num1) * int(num2)
    operacion = Lab01_tarea(num1=num1, num2=num2, tipo_operacion="Multiplicación", resultado=resultado)
    operacion.save()
    return render(request, 'lab01_tarea/vista.html', {'mensaje': f"La multiplicación de {num1} * {num2} = {resultado}"})


