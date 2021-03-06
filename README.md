# Integarting Celery with Django to asynchronous tasks π
Integrating π **Celery** with Django via **Redis server** ,To-Do asynchronously πtask without stopping the main-flow π of Django-project .It increase your speed π and user experience π€΅ of website .
This repo explain how to setup Celery,and integrate it with the Django-Framework.

**Note : Steps to steup Celery on production-side is different**
<br>

π [Reference link to setup Celery on production side](https://medium.com/koko-networks/a-complete-guide-to-production-ready-celery-configuration-5777780b3166)

# Approach π
Celery package help us to asynchronous tasks on different worker π₯οΈ ,That is on Redis server. The Celery also have some great features in scheduling π task after a certain period of time.
The tasks are excuted on different server *(Redis server)*, and are not run on Django-Server.If we run long and complicated tasks on django server it will reduced the efficiency of website

<br>

Modern users expect pages to load instantaneously β‘, to solve this we consider many solutions like multiprocessing, multithreading π§΅, asynchronous functions using async/await or the Message Queues.

<br>

<p align="center">
  <img src="https://miro.medium.com/max/1050/0*ppAh-AtPSXGbUAvE.png" style="height:50%;width:50%;">
</p>

# Installation/Dependencies πΎ

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following modules and packages. 

```bash
pip install -r requirements.txt
```

### [Download Redis server form here](https://download.redis.io/releases/redis-6.2.6.tar.gz) β¬οΈ 

# Usage π­

*Open terminal and write following commands π*


To run Celery worker
```bash
celery -A your_django_project_name.celery worker --pool=solo -l info
```
And in separate terminal run django server
```bash
python manage.py runserver
```

### Updating SMTP settings for sending mails π¨
Change the settings for the sender-mail credential in the `settings.py` file , enter the sender mail and sender mail-password (SMTP configuartion)


# Making tasks π
Task are python functions which can be called in the django-project and also be scheduled at particular time.
Task-function can be written in `task.py` file and can be imported anywhere in the project

```
@task()
def Send_Mail_With_Celery(email):
  your function goes here....
  return "done"
```

calling function

```
Send_Mail_With_Celery.delay(args)
```

# Purpose π’
Increase Speed β‘ and User-experience of website



#### Sending mail using Celery π
<p align="center">
  <img src="https://github.com/Developer-R-7/Celery-Integration-Django/blob/master/static/Screenshots/WithCelery.gif" style="height:50%;width:50%;">
</p>

### Sending mail without using Celery β

<p align="center">
  <img src="https://github.com/Developer-R-7/Celery-Integration-Django/blob/master/static/Screenshots/WithoutCelery.gif" style="height:50%;width:50%;">
</p>

**NOTE the difference : Celery does not stoped the next page from loading and done the task on worker whereas Without using Celery it took almost 3 seconds β , to load next page**

This is just a small-function but imagine making operations on large user-database ,it would be not good βΉοΈ 

# Reference π
[Setup Celery in Django to asynchronous tasks](https://realpython.com/asynchronous-tasks-with-django-and-celery/)

# Contributing π€΅
Pull requests are welcome π€. For major changes, please open an issue first to discuss what you would like to change.
