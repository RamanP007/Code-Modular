from .models import Contact
from django.shortcuts import render, HttpResponse
# from .models import models

# Create your views here.
def home(request):
    # return HttpResponse("This is My Homepage")
    context = {"Name": "Harry", "Course" : "Django"}
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("This is My About page")
    return render(request, 'about.html')
    

def projects(request):
    # return HttpResponse("This is My Projects")
    return render(request, 'projects.html')

def contact(request):
    if request.method=='POST':
        print('This is POST')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print('DAta has been written into the Database')
    # return HttpResponse("This is My Contact")
    return render(request, 'contact.html')



