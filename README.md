# Integarting Celery with Django to asynchronous tasks 📃
Integrating 🔗 **Celery** with Django via **Redis server** ,To-Do asynchronously 👀task without stopping the main-flow 📃 of Django-project . It increase your speed 🚀 and user experience 🤵 of website .
This repo explain how to setup Celery,and integrate it with the Django-Framework.

**Note : Steps to steup Celery on production-side is different**
<br>

🏁 [Reference link to setup Celery on production side](https://medium.com/koko-networks/a-complete-guide-to-production-ready-celery-configuration-5777780b3166)

# Approach 🏁
Celery package help us to asynchronous tasks on different worker 🖥️ ,That is on Redis server. The Celery also have some great features in scheduling 🕐 task after a certain period of time.
The tasks are excuted on different server *(Redis server)*, and are not run on Django-Server.If we run long and complicated tasks on django server it will reduced the efficiency of website

<br>

Modern users expect pages to load instantaneously ⚡, to solve this we consider many solutions like multiprocessing, multithreading 🧵, asynchronous functions using async/await or the Message Queues.

<br>

<img src="https://miro.medium.com/max/1050/0*ppAh-AtPSXGbUAvE.png" style="height:50%;width:50%;">

# Installation/Dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following modules and packages. 

```bash
pip install Django
```
```bash
pip install celery
```
```bash
pip install redis
```