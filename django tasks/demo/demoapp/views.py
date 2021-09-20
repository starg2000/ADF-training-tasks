from django.http import HttpResponse
from django.shortcuts import render
from .models import Request_Info, Response_Info
import json
from django.views import View
from .validate import Validate


# Create your views here.
class Home(View):
	def get(self, request):
		return render(request,"demoapp/form.html")

class Adddata(View):
	def post(self, request):
		response =""
		reason=""
		fname = request.POST["fn"]
		lname = request.POST["ln"]
		dob = request.POST["dob"]
		gender = request.POST["gender"]
		nation = request.POST["nation"]
		city = request.POST["city"]
		state = request.POST["state"]
		pin = request.POST["pin"]
		qual = request.POST["qual"]
		salary = request.POST["sal"]
		pan = request.POST["pan"]
		
		valobj =  Validate()
		valobj.validate_gns(gender, nation, state)
		valobj.validate_salary(salary)
		valobj.validate_age(dob, gender)
		valobj.validate_pan(pan)
		valobj.validate_text(fname)
		valobj.validate_text(lname)
		valobj.validate_text(city)
		valobj.validate_text(qual)

		reason = valobj.return_status()
		if reason =="":
			response ="success"
		else:
			response="fail"
		reqform= Request_Info.objects.create(firstname=fname, lastname=lname, dob=dob, gender=gender,
			nationality=nation, city=city, state=state, pincode=pin, qualification=qual,
			salary=salary, pan=pan)
		reqform.save()
		res = json.dumps({"response":response,"reason":reason})
		obj = Response_Info.objects.create(resid=None, response=str(res))
		obj.save()
		js=json.loads(res)
		return render(request,"demoapp/results.html",{"json":js,'obj':Request_Info.objects.all()})
	def get(self, request):
		return HttpResponse("Something went wrong")
