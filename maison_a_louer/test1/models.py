from django.db import models

# Create your models here.

class User(models.Model):
	username=models.CharField(max_length=100,unique=True)
	password=models.CharField(max_length=100)
	public_key=models.TextField()
	private_key=models.TextField()



class Maison(models.Model):
    emplacement=models.ForeignKey('Emplacement',on_delete=models.CASCADE)
    nombre_de_chambre=models.IntegerField(blank=True,null=True)
    nombre_de_personne=models.IntegerField()
    info=models.TextField()
    prix=models.IntegerField()
    nombre_de_place_restant=models.IntegerField()
    nombre_de_chambre_inscrit=models.IntegerField(blank=True,null=True,default=0)
    image=models.ImageField(upload_to="photos/")

class Chambre(models.Model):
    maison=models.ForeignKey('Maison',on_delete=models.CASCADE)
    nombre_de_personne=models.IntegerField()
    info=models.TextField()
    prix=models.IntegerField()
    nombre_de_place_restant=models.IntegerField()
    image=models.ImageField(upload_to="photos/")


class Allocation(models.Model):
    nom_allocateur=models.CharField(max_length=100)
    prenom_allocateur=models.CharField(max_length=100)
    maison=models.ForeignKey('Maison',on_delete=models.CASCADE)
    


class Emplacement(models.Model):
	emplacement=models.CharField(max_length=100);
	def __str__(self):
		return self.emplacement
