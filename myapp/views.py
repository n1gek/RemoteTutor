from django.shortcuts import render, redirect
from . models import Student
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.http import JsonResponse
from .models import Message
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')

def subject_selection(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
    
    return render(request, 'subject.html', {'subject': subject})
        

def checkview(request):
    email_address = request.POST.get('email')
    password = request.POST.get('password')
    subject = request.POST.get('subject')
        
        #check for the email
    user = Student.objects.filter(email=email_address).first()
    if user:
            if check_password(password, user.password):
                # if the password is correct:
                return redirect('/room?subject=' + subject + '&email=' + email_address)
            else:
                return render(request, 'subject.html', {'subject': request.POST.get('subject'), 'error': 'Incorrect password'})
    else:
            #when the email does not exist, so we have to create a new one
            hashed_password = make_password(password)
            Student.objects.create(email=email_address, password=hashed_password)
            return redirect('/room?subject=' + subject + '&email=' + email_address)

def room(request):
     user = request.GET.get('email')
     subject = request.GET.get('subject')

 
     return render(request, 'chat.html',
                   {'user': user,
                    'subject': subject
                    })

def send(request):
    message = request.POST['message']
    username = request.POST['email']

    user = Student.objects.get(email=username)

    new_message = Message.objects.create(value=message, user=user)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request):
     email = request.GET.get('email')
     subject = request.GET.get('subject')
     user = Student.objects.get(email=email) 

     messages = Message.objects.filter(user=user)
     return JsonResponse({"messages":list(messages.values())})
