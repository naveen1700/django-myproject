from django.shortcuts import render
from django.http import HttpResponse
from naveen.models import Contact

# Create your views here.
def index(request):
    context = {
        'variable': "This is sent"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')

        if name and phone and email and desc:
            contact = Contact(name=name, phone=phone, email=email, desc=desc)
            contact.save()
            return render(request, "contact.html", {"success": True})
        else:
            return render(request, "contact.html", {"error": "All fields are required!"})

    return render(request, 'contact.html')


