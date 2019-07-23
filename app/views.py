from django.shortcuts import render
from .models import Delivery
# Create your views here.

def main_page(request):
    delivery = Delivery.objects.all()
    print(delivery)
    return render(request,'app/main_page.html',{'delivery':delivery})
