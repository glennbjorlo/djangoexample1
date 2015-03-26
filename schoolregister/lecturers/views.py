from django.shortcuts import render
from django.http import HttpResponse
#from django.http import JsonResponse

from lecturers.models import Lecturer

# Create your views here.

def lecturer_listing(request):
	lecturers = Lecturer.objects.all()
	context = {'lecturers': lecturers}
	return render(request, 'lecturers/lecturer_listing.html', context)

def lecturer_details(request, lecturer_id):
	lecturer = Lecturer.objects.get(pk=lecturer_id)
	context = {'lecturer': lecturer}
	return render(request, 'lecturers/lecturer_details.html', context)

	
