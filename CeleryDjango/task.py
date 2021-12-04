from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .celery import app



@app.task
def Send_Mail_With_Celery(email):
    html_content = render_to_string("email.html",{'email':email})
    text_content = strip_tags(html_content)
    email_con = EmailMultiAlternatives('Hello, Greetings from Rushi',text_content,settings.EMAIL_HOST_USER,[email]) 
    email_con.attach_alternative(html_content,"text/html")
    email_con.send()
    return "Done"
