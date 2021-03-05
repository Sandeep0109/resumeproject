from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    contaxt={'home':'active'}
    return render(request,'core/home.html',contaxt)

def contact(request):
    if request.method=="POST":
        print(request) 
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        subject=request.POST.get('subject','')
        massage=request.POST.get('massage','')
        print(name,email,subject,massage)

        contact= Contact(name=name,email=email,subject=subject,massage=massage)
        contact.save()

    contaxt={'contact':'active'}
    return render(request,'core/contact.html' ,contaxt)    