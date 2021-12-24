from django.db import models
#from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

class Categoria(models.Model):
	detalle = models.CharField(max_length=255)
#	autor = models.ForeignKey(Comentario, on_delete=models.CASCADE, null=True)

	class Meta:
		db_table="Categoria"

	def __str__(self):
		return self.detalle

class Usuario(AbstractUser):
	dni = models.IntegerField(null=True, blank=True)
	# foto = models.ImageField()
	es_administrador = models.BooleanField(default=False)
	es_escritor = models.BooleanField(default=False)

	class Meta:
		db_table="usuario"

	def __str__(self):
		return f"{self.username}"


class Post(models.Model):
	nombre = models.CharField(max_length=255)
	detalle = models.TextField(max_length=1000)
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True,blank=True)
	estado = models.BooleanField(default=False,null=True,blank=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True,blank=True)
	
	#comentarios = models.ManyToManyField(Comentario,null=True, blank=True)

	class Meta:
		db_table="post"

	def __str__(self):
		return self.nombre




class Comentario(models.Model):
	detalle = models.TextField(max_length=1000)
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True,blank=True)
	posteo = models.ForeignKey( Post,on_delete=models.CASCADE,null=True,blank=True)


	class Meta:
		db_table="Comentario"

	def __str__(self):
		return self.detalle

