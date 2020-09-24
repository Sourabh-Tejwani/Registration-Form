from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

d=User()

def formpage(request):
	if(request.method=='POST'):
		print("hello")
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
		u.password=request.POST.get('password')
		u.save() 	
		return redirect('/')


		print(request.POST.get('gender'))	
	return render(request = request,template_name="formuser.html",)


def loginpage(request):
	if(request.method=='POST'):
		for t in User.objects.all():
			if(t.email==request.POST.get('email')):
				if(t.password==request.POST.get('password')):
					global d
					d=t
					print("URL ",str(t.picture))
					request.session['name'] = t.first_name
					request.session['last_name']=t.last_name
					request.session['email']=t.email
					request.session['date_of_birth']=str(t.date_of_birth)
					request.session['contact']=t.contact
					request.session['gender']=t.gender
					request.session['address']=t.address
					request.session['city']=t.city
					request.session['state']=t.state
					request.session['country']=t.country
					request.session['picture']=str(t.picture)
					return redirect('profile/',)
				else:
					return render(request=request,template_name="login.html",context={"error":"password does not match",})
		return render(request=request,template_name="login.html",context={"error":"User does not found",})
	return render(request=request,template_name="login.html",context={"error":"",})

def profile(request):
	if request.method=='POST' and request.FILES['myfile']:
		myfile=request.FILES['myfile']
		fs=FileSystemStorage()
		filename=fs.save(myfile.name,myfile)
		url=fs.url(filename)
		d.picture=url
		d.save()
		request.session['name'] = d.first_name
		request.session['last_name']=d.last_name
		request.session['email']=d.email
		request.session['date_of_birth']=str(d.date_of_birth)
		request.session['contact']=d.contact
		request.session['gender']=d.gender
		request.session['address']=d.address
		request.session['city']=d.city
		request.session['state']=d.state
		request.session['country']=d.country
		request.session['picture']=d.picture
		return redirect('')

	else:
			return render(request=request,template_name="profile.html",)
