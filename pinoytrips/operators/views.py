from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Operator

def index(request):
	list_of_all_operators = Operator.objects.all()
	template = loader.get_template('operators/index.html')
	context = RequestContext(request, {
		'list_of_all_operators': list_of_all_operators,		
	})
	return HttpResponse(template.render(context))

def detail(request, name_id):
	operator = get_object_or_404(Operator, pk=name_id)
	return render(request, 'operators/detail.html', {'operator': operator})

def results(request, name):
	response = "You're looking at the results of operator %s."
	return HttpResponse(response % name)

def change_destination(request, name_id):
    return HttpResponse("You're changing operator %s." % name)