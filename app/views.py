from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    template_name='app/index.html'
    return render(request,template_name)
    

def contact(request):
    if request.method == 'POST':
        email_r=request.POST.get('email')
        first=request.POST.get('firstName')
        last=request.POST.get('lastName')
        phone=request.POST.get('phone')
        email_a=['akshitagarg275@gmail.com']
        c=Contact(firstName=first,lastName=last,email=email_r,phone=phone)
        subject = 'Thank you for visiting to our site'
        message = ' It  means a alot to us. We will get back to you within 12 hrs '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_r,]
        subject2='A new user added'
        message2=first+' with '+email_r+' has visited.'
        send_mail( subject, message, email_from, recipient_list )
        send_mail( subject2, message2, email_from, email_a )
        c.save()
        
        model=Contact.objects.all
        template_name='app/table.html'
        context={'model':model}

        return render(request,template_name,context)

    else:
        return render(request,'app/index.html')

def dashboard(request):
    
    model=contact.objects.all
    if model is not None:
        template_name='mysite/table.html'
        context={'model':model}
        return render(request,template_name,context)
    else:
        return render(request,'app/index.html')