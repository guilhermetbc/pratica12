from django.db import models

# Create your models here.

class Banda(models.Model):
	"""docstring for Banda"""
	nome = models.CharField(max_length=100)
	musicos = models.ManyToManyField('Musico')
	n_integrantes = models.IntegerField()
	estilo = models.ForeignKey('EstiloMusical',on_delete=models.CASCADE)
	data_criacao = models.DateField()

	def __str__():
		return self.nome	
				

class Musico(models.Model):
	"""docstring for Musico"""
	nome = models.CharField(max_length=100)
	data_nascimento  = models.DateField()

	def __str__():
		return self.nome
				

class EstiloMusical(models.Model):
	"""docstring for EstiloMusical"""
	nome = models.CharField(max_length=100)

	def __str__():
		return self.nome
		