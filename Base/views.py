from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
# Create your views here.

def home(request):
    return render(request,'home.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')  # fixed key from 'contact' to 'content'
        number = request.POST.get('number')
        print(name, email, number, content)

        if len(name) < 2 or len(name) > 30:
            messages.error(request, 'Length of name should be greater than 2 and less than 30 characters')
            return render(request, 'home.html')
        if len(email) < 5 or len(email) > 40:
            messages.error(request, 'Invalid email, try again')
            return render(request, 'home.html')
        if len(number) < 7 or len(number) > 13:
            messages.error(request, 'Invalid number, try again')
            return render(request, 'home.html')

        ins = Contact(name=name, email=email, content=content, number=number)
        ins.save()
        messages.success(request, 'Thank you for contacting me! Your message has been saved.')
        return render(request, 'home.html')
    return render(request, 'home.html')