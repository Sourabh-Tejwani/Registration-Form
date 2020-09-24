from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
	fieldsets=[
			("Name",{"fields":["picture","first_name","last_name","password"]}),
			("Information",{"fields":["email","date_of_birth","contact","gender"]}),
			("Address",{"fields":["address","city","state","country"]}),
	]



admin.site.register(User,UserAdmin)