from django.shortcuts import render
from django.http import JsonResponse
from .models import Bank_Detail
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
	return render(request,"details/index.html")

@csrf_exempt
def branchdetail(request):

	data={}
	if request.method == 'POST':
		ifsc=request.POST.get('ifsc')
		if "ifsc" not in request.POST:
			data["success"]=False
			data["message"]="Enter ifsc code."
			return JsonResponse(data,safe=False)

		try:
			detail=Bank_Detail.objects.get(ifsc=ifsc)
		except Exception as e:
			data["success"]=False
			data["message"]="Details for your ifsc does not exist."
			return JsonResponse(data,safe=False)

		details=[]
		d={
			'ifsc':detail.ifsc,
			'bank_id':detail.bank_id,
			'branch':detail.branch,
			'address':detail.address,
			'city':detail.city,
			'district':detail.district,
			'state':detail.state,
			'bank_name':detail.bank_name
		}
		details.append(d)
		data["success"]=True
		data["details"]=details
		return JsonResponse(data,safe=False)
	else:
		data["success"]=False
		data["message"]="Method not allowed."

@csrf_exempt
def allbranchCity(request):

	data={}
	if request.method == 'POST':
		name=request.POST.get('name')
		city=request.POST.get('city')

		if "city" not in request.POST and "name" not in request.POST:
	            data["success"] = False
	            data["message"] = "Enter the city and bank name."
	            return JsonResponse(data,safe=False)

		if "city" not in request.POST:
			data["success"] = False
			data["message"] = "Enter the city."
			return JsonResponse(data,safe=False)

		if "name" not in request.POST:
			data["success"] = False
			data["message"] = "Enter the bank name."
			return JsonResponse(data,safe=False)
	        
		allbranch = Bank_Detail.objects.filter(city=city,bank_name=name)

		if allbranch.count() == 0:
			data["success"] = False
			data["message"] = "No details found for the given city and bank name."
			return JsonResponse(data,safe=False)
	    
		branches = []

		for obj in allbranch:
			branch = {
				'ifsc' : obj.ifsc,
				'bank_id': obj.bank_id,
				'branch' : obj.branch,
				'address' : obj.address,
				'district' : obj.district,
				'state' : obj.state,
			}
			branches.append(branch)
			branch = {}

		data["success"] = True
		data["message"] = branches

		return JsonResponse(data,safe=False)     

	else:
		data["success"] = False
		data["message"] = "Method not allowed."    

		return JsonResponse(data,safe=False)


import pandas as pd
def csvload(request):
	data=pd.read_csv('/home/subhash/test/bank/details/bank_branches.csv')
	print(len(data))
	for i in range(0,10001):
		detail=Bank_Detail()
		detail.id=i+1
		detail.ifsc=data["ifsc"][i]
		detail.bank_id=data["bank_id"][i]
		detail.branch=data["branch"][i]
		detail.address=data["address"][i]
		detail.city=data["city"][i]
		detail.district=data["district"][i]
		detail.state=data["state"][i]
		detail.bank_name=data["bank_name"][i]

		detail.save()
