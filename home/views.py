from django.shortcuts import render,HttpResponse,redirect
from home.models import contact
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")
def Contact(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        Text = request.POST.get("Text")
        contactobj = contact(
            firstName=firstName,
            lastName=lastName,
            email=email,
            Text=Text,
            date=datetime.now(),
        )
        contactobj.save()
        return render(request,'thanks.html')
    return render(request,"contact.html")