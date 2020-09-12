from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def formpage(request):
	if(request.method=='POST'):
		u=User()
		u.first_name=request.POST.get('firstname')
		u.last_name=request.POST.get('lastname')
		u.email=request.POST.get('email')
		u.date_of_birth=request.POST.get('birthday')
		u.contact=request.POST.get('contactnumber')
		u.gender=request.POST.get('gender')
		u.address=request.POST.get('address')
		u.state=request.POST.get('state')
		u.city=request.POST.get('city')
		u.country=request.POST.get('country')
		u.save() 	
		return render(request = request,template_name="submit.html",)


		print(request.POST.get('gender'))	
	return render(request = request,template_name="form.html",)