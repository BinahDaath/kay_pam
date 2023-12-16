from django.http import HttpResponse
from django.shortcuts import render
import re
from test1.models import *
from test1.forms import *
import json
import rsa
import datetime

# Create your views here.

search_form=Search_form()

def view_home(request):
	id=request.GET.get("id")
	home=Maison.objects.filter(id=int(idd))[0]
	home={"id":home.id,"emplacement":home.emplacement,"nombre_de_personne":home.nombre_de_personne,"info":home.info,"prix":home.prix,"nombre_de_place_restant":home.nombre_de_place_restant}
	return HttpResponse(json.dumps(home))
	
	
	


def homes_liste(request):
	search_form=Search_form()
	r=request.GET
	id=0
	id
	prix__gte=0
	nombre_de_personne__gte=0
	nombre_de_place_restant__gte=0
	next=re.sub("\?.*","?",request.build_absolute_uri())
	if ("id" in r) and (len(r["id"]) != 0):
		id=int(request.GET.get("id"))
	if "nombre_de_personne__gte" in r and (len(r["nombre_de_personne__gte"]) != 0):
		nombre_de_personne__gte=int(request.GET.get("nombre_de_personne__gte"))
		next+="&nombre_de_personne__gte="+str(nombre_de_personne__gte)
	if "nombre_de_place_restant__gte" in r and (len(r["nombre_de_place_restant__gte"]) != 0):
		nombre_de_place_restant=request.GET.get("nombre_de_place_restant__gte")
	if "prix__gte" in r and (len(r["prix__gte"]) != 0):
		prix__gte=int(request.GET.get("prix__gte"))
		next+="&prix__gte="+str(prix__gte)
	homes=Maison.objects.filter(id__gte=id,nombre_de_personne__gte=nombre_de_personne__gte,prix__gte=prix__gte,nombre_de_place_restant__gte=nombre_de_place_restant__gte)
	if "emplacement" in r and (len(r["emplacement"]) != 0):
		emplacement=Emplacement.objects.filter(id=int(request.GET.get("emplacement")))[0]
		next+="&emplacement="+str(request.GET.get("emplacement"))
		homes=homes.filter(emplacement=emplacement)
	if "nombre_de_personne" in r and (len(r["nombre_de_personne"]) != 0):
		nombre_de_personne=int(request.GET.get("nombre_de_personne"))
		next+="&nombre_de_personne="+str(nombre_de_personne)
		homes=homes.filter(nombre_de_personne=nombre_de_personne)
	if "nombre_de_personne__lte" in r and (len(r["nombre_de_personne__lte"]) != 0):
		nombre_de_personne__lte=int(request.GET.get("nombre_de_personne__lte"))
		homes=homes.filter(nombre_de_personne__lte=nombre_de_personne__lte)
		next+="&nombre_de_personne__lte="+str(nombre_de_personne__lte)
	if "nombre_de_place_restant" in r and (len(r["nombre_de_place_restant"]) != 0):
		nombre_de_place_restant=request.GET.get("nombre_de_place_restant")
		homes=homes.filter(nombre_de_place_restant=nombre_de_place_restant)
		next+="&nombre_de_place_restant="+str(nombre_de_place_restant)
	if "nombre_de_place_restant__lte" in r and (len(r["nombre_de_place_restant__lte"]) != 0):
		nombre_de_place_restant__lte=request.GET.get("nombre_de_place_restant__lte")
		homes=homes.filter(nombre_de_place_restant__lte=nombre_de_place_restant__lte)
		next+="&nombre_de_place_restant__lte="+str(nombre_de_place_restant__lte)
	if "prix" in r and (len(r["prix"]) != 0):
		prix=int(request.GET.get("prix"))
		homess=homes.filter(prix=prix)
		next+="&prix="+str(prix)
	if "prix__lte" in r and (len(r["prix__lte"]) != 0):
		prix__lte=int(request.GET.get("prix__lte"))
		homes=homes.filter(prix__lte=prix__lte)[:10]
		next+="&prix__lte="+str(prix__lte)
	id__gte=id+10
	next+="&id="+str(id__gte)
	#homes={"id":homes.id,"emplacement":homes.emplacement,"nombre_de_personne":homes.nombre_de_personne,"info":homes.info,"prix":homes.prix,"nombre_de_place_restant":homes.nombre_de_place_restant}
	return render(request, 'test1/liste.html', locals())
	
	
	
def add_home(request):
	if request.method == 'POST':
		form = Maison_form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			form = Maison_form()
	else:
		form = Maison_form()
	return render(request, 'test1/add_home.html', locals())







def add_room(request):
	if request.method == 'POST':
		form = Chambre_form(request.POST,request.FILES)
		if form.is_valid():
			room=form.save(commit=False)
			maison=room.maison
			if maison.nombre_de_chambre_inscrit < maison.nombre_de_chambre:
				maison.nombre_de_chambre_inscrit+=1
				maison.save()
				room.save()
			form = Chambre_form()
	else:
		form = Chambre_form()
	return render(request, 'test1/add_room.html', locals())




def add_emplacement(request):
	if request.method == 'POST':
		form = Emplacement_form(request.POST)
		if form.is_valid():
			form.save()
			form = Emplacement_form()
	else:
		form = Emplacement_form()
	return render(request, 'test1/add_home.html', locals())






def room_liste(request):
	search_form=Search_form()
	r=request.GET
	id=0
	id
	prix__gte=0
	nombre_de_personne__gte=0
	nombre_de_place_restant__gte=0
	next=re.sub("\?.*","?",request.build_absolute_uri())
	if ("id" in r) and (len(r["id"]) != 0):
		id=int(request.GET.get("id"))
	if "nombre_de_personne__gte" in r and (len(r["nombre_de_personne__gte"]) != 0):
		nombre_de_personne__gte=int(request.GET.get("nombre_de_personne__gte"))
		next+="&nombre_de_personne__gte="+str(nombre_de_personne__gte)
	if "nombre_de_place_restant__gte" in r and (len(r["nombre_de_place_restant__gte"]) != 0):
		nombre_de_place_restant=request.GET.get("nombre_de_place_restant__gte")
	if "prix__gte" in r and (len(r["prix__gte"]) != 0):
		prix__gte=int(request.GET.get("prix__gte"))
		next+="&prix__gte="+str(prix__gte)
	homes=Chambre.objects.filter(id__gte=id,nombre_de_personne__gte=nombre_de_personne__gte,prix__gte=prix__gte,nombre_de_place_restant__gte=nombre_de_place_restant__gte)
	if "emplacement" in r and (len(r["emplacement"]) != 0):
		emplacement=Emplacement.objects.filter(id=int(request.GET.get("emplacement")))[0]
		next+="&emplacement="+str(request.GET.get("emplacement"))
		homes=homes.filter(maison__emplacement=emplacement)
	if "nombre_de_personne" in r and (len(r["nombre_de_personne"]) != 0):
		nombre_de_personne=int(request.GET.get("nombre_de_personne"))
		next+="&nombre_de_personne="+str(nombre_de_personne)
		homes=homes.filter(nombre_de_personne=nombre_de_personne)
	if "nombre_de_personne__lte" in r and (len(r["nombre_de_personne__lte"]) != 0):
		nombre_de_personne__lte=int(request.GET.get("nombre_de_personne__lte"))
		homes=homes.filter(nombre_de_personne__lte=nombre_de_personne__lte)
		next+="&nombre_de_personne__lte="+str(nombre_de_personne__lte)
	if "nombre_de_place_restant" in r and (len(r["nombre_de_place_restant"]) != 0):
		nombre_de_place_restant=request.GET.get("nombre_de_place_restant")
		homes=homes.filter(nombre_de_place_restant=nombre_de_place_restant)
		next+="&nombre_de_place_restant="+str(nombre_de_place_restant)
	if "nombre_de_place_restant__lte" in r and (len(r["nombre_de_place_restant__lte"]) != 0):
		nombre_de_place_restant__lte=request.GET.get("nombre_de_place_restant__lte")
		homes=homes.filter(nombre_de_place_restant__lte=nombre_de_place_restant__lte)
		next+="&nombre_de_place_restant__lte="+str(nombre_de_place_restant__lte)
	if "prix" in r and (len(r["prix"]) != 0):
		prix=int(request.GET.get("prix"))
		homess=homes.filter(prix=prix)
		next+="&prix="+str(prix)
	if "prix__lte" in r and (len(r["prix__lte"]) != 0):
		prix__lte=int(request.GET.get("prix__lte"))
		homes=homes.filter(prix__lte=prix__lte)[:10]
		next+="&prix__lte="+str(prix__lte)
	if "maison" in r and (len(r["maison"]) != 0):
		maison=Maison.objects.filter(id=int(request.GET.get("maison")))[0]
		next+="&maison="+str(request.GET.get("maison"))
		homes=homes.filter(maison=maison)
	id__gte=id+10
	next+="&id="+str(id__gte)
	#homes={"id":homes.id,"emplacement":homes.emplacement,"nombre_de_personne":homes.nombre_de_personne,"info":homes.info,"prix":homes.prix,"nombre_de_place_restant":homes.nombre_de_place_restant}
	return render(request, 'test1/liste_chambre.html', locals())
