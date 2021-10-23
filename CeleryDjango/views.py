from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.conf import settings 
from . import task
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags



def Send_Mail_Without_Celery(email):
    html_content = render_to_string("email.html",{'email':email})
    text_content = strip_tags(html_content)
    email_con = EmailMultiAlternatives('Hello, Greetings from Rushi',text_content,settings.EMAIL_HOST_USER,[email]) 
    email_con.attach_alternative(html_content,"text/html")
    email_con.send()


def index(request):
    if request.method == "POST":
        mail_to_send_hello_message = request.POST.get("email")

        if settings.USE_CELERY:                      
            # Sending mail using celery
            task.Send_Mail_With_Celery.delay(mail_to_send_hello_message)
            return render(request,'index.html',{'send_mail':True})
        else:                                        
            # Sending mail without using celery
            Send_Mail_Without_Celery(mail_to_send_hello_message)
            return render(request,'index.html',{'send_mail':True})
    
    else:
        return render(request,'index.html',{'send_mail':False})