from django.db import models

class Empresa(models.Model):
	id_empleador = models.CharField(max_length=15)
	razon_social = models.CharField(max_length=50, null=True)
	celular = models.IntegerField(null=True)
	telefono = models.IntegerField(null=True)
	email =  models.EmailField(max_length=50, null=True)
	direccion =  models.CharField(max_length=100, null=True)
	comuna =  models.CharField(max_length=50, null=True)
	region =  models.CharField(max_length=30, null=True)
	cant_afiliados =  models.PositiveIntegerField(null=True)
	fecha_ultima_actualizacion = models.DateTimeField(auto_now=True, null=True)
	nombre_contacto = models.CharField(max_length=50, null=True)

	def __str__(self):
		return(f"{self.razon_social}")

class Gestion(models.Model):
	class TipoGestion(models.TextChoices):
		CORREO = 'CO'
		LLAMADA = 'LL'
		VIDEOLLAMADA = 'VL'
		REUNION = 'RE'
		VISITA = 'VI'
		MENSAJE = 'ME'	
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	fecha_hora = models.DateTimeField(auto_now_add=True)
	tipo = models.CharField(max_length=2, choices=TipoGestion.choices) 
	estado = models.CharField(max_length=20)
	comentarios = models.TextField(null=True)

	def __str__(self):
		return(f"{self.tipo} del {self.fecha_hora}")

class Recordatorio(models.Model):
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=20)
	fecha_alerta = models.DateTimeField()
	observacion = models.TextField(null=True)