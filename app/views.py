from django.shortcuts import render,redirect
from . models import *
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
	if request.method=='POST':
		name = request.POST.get('name')
		amount = int(request.POST.get('amount'))*100
		client = razorpay.Client(auth=("rzp_test_HeL5OoMHfm4g2R","JRs6OtohKAXs8bE1skBmMZoQ"))
		payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
		
		coffee = Cofee(name=name , amount=amount, payment_id = payment['id'])
		coffee.save()
	return render(request, "index.html",{'payment':payment})



@csrf_exempt
def success(request):
	if request.method == 'POST':
		a = request.POST
		print(a)
	return render(request,'success.html')
