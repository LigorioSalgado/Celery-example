from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add

def index(request):

	if request.method == 'GET':
		suma = add.delay(2,3)
		result = suma.get()
		rest = 2-3
		mult = 2*3
	
		message = "<p> mi suma es : "+str(result)+"mi resta es: "+str(rest)+"mi multiplicacion es: "+str(mult)+"</p>"

		return HttpResponse(message)
	return HttpResponse('LOL')

# Create your views here.



