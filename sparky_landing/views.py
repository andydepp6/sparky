from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sparky_landing.models import *
from sparky_landing.forms import *

# Create your views here.

def index(request):

	return render(request,'index.html')

@csrf_exempt
def save(request):

	if request.is_ajax():

		if request.method == 'POST':

			form = Register_t(request.POST)

			if form.is_valid():

				try:
					try:
						Register.objects.get(email=request.POST['email'])
						message = '3'
					except:
						Register(name=request.POST['name'],email=request.POST['email']).save()
						message = '0'
				
				except:
					message = '1'

				return HttpResponse(message)
			else:

				message = '2'
				return HttpResponse(message)
		else:

			message = "Acceso no autorizado"

			return HttpResponse(message)
	else:
		message = "Acceso no autorizado"

	return HttpResponse(message)

def handler404(request):
	return render(request,'404.html')

def handler500(request):
	return render(request,'500.html')