from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hello from Haynes',
    'Hello there. This is an automated message.',
    'cromarties2913@gmail.com',
    ['hrc345@gmail.com','hrc245@gmail.com'],
    fail_silently=False
    )

     
    return render(request,'send/index.html')