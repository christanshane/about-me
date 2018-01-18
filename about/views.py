from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index (request):
	template = loader.get_template('about/index.html')
	return HttpResponse (template.render({},request))

def gallery(request):
	template = loader.get_template('about/gallery.html')
	return HttpResponse(template.render({},request))