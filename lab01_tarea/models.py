from django.db import models

class Lab01_tarea(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    tipo_operacion = models.CharField(max_length=20)
    resultado = models.IntegerField()

    def __str__(self):
        return f"Primer digito: {self.num1}, Segundo digito: {self.num2}, Operación: {self.tipo_operacion}, Resultado: {self.resultado}"
    
