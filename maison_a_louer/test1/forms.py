from test1.models import *
from django import forms
class User_form(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'



class Maison_form(forms.ModelForm):
	class Meta:
		model = Maison
		fields = '__all__'




class Allocation_form(forms.ModelForm):
	class Meta:
		model = Allocation
		fields = '__all__'
		
class Emplacement_form(forms.ModelForm):
	class Meta:
		model = Emplacement
		fields = '__all__'	

class Chambre_form(forms.ModelForm):
	class Meta:
		model=Chambre
		fields='__all__'
		
class Search_form(forms.Form):
	emplacement=forms.ModelChoiceField(Emplacement.objects.all(),required=False)
	nombre_de_personne=forms.IntegerField(required=False)
	nombre_de_personne__gte=forms.IntegerField(label="nombre de personne superieur ou egal a",required=False)
	nombre_de_personne__lte=forms.IntegerField(label="nombre de personne inferieur ou egal a",required=False)
	nombre_de_place_restant=forms.IntegerField(required=False)
	nombre_de_place_restant__gte=forms.IntegerField(label="nombre de place restant superieur ou egal a",required=False)
	nombre_de_place_restant__lte=forms.IntegerField(label="nombre de place restant inferieur ou egal a",required=False)
	prix=forms.IntegerField(required=False)
	prix__lte=forms.IntegerField(label="prix inferieur ou egal a",required=False)
	prix__gte=forms.IntegerField(label="prix superieur ou egal a",required=False)
	
