from django.shortcuts import render
from django.core.mail import  send_mail

# from django.http.response import HttpResponse 



def home(request):

    if request.method == "POST":
        # name = request.POST.get('fullname')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')

        name = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        data ={
        
           'name': name,
           'email': email,
           'subject': subject,
           'message': message
       }

        message ='''
        New Message:{}

        From:{}
        '''.format(data['message'],data['email'])
       
        send_mail( data['message'],message,'sanjipshrestha6@gmail.com',['sanjipshrestha6@gmail.com'],fail_silently=False,)
        # return render(request, 'home.html',{'name': name},{'email':email},{'subject':subject},{'message':message})




    else:

        return render(request, 'home.html',{})