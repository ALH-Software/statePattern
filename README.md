# Django Sample - STATE Pattern
A simple example of Django

## About my project
The following task has (New, In Progress, Done) statuses and in each stays the object can be manipulated in different ways. Here, a project
in Python Django with its API using the design pattern “STATE” to provide the solution.

New:
* edit title
* edit description

In Progress:
* Link 2 tasks together

Done:
* Cannot prform any operation.

## Installation

First of all, You should download the source code for this project and run it on your local machine.

Of course, you should have python 3 installed on your PC.

Now installing Django

```bash
pip install Django
```

Installing django rest framework

```bash
pip install djangorestframework
```

Adding CORS headers allows your resources to be accessed on other domains:

```bash
pip install django-cors-headers
```

## Run the project

Now make migrations for the model. Go to the base folder containing ```manage.py``` and run

```bash
python manage.py makemigrations
```

Now migrate this file to create a database structure for this.

```bash
python manage.py migrate
```

Now, run the web server:

```bash
python manage.py runserver
```

and then browser the: 

```bash
http://127.0.0.1:8000
```


## Details
Project has APIs for the above functionalities, in addition to front-end using jQuery.

### Available URLs

```json
   1. admin/
   2. api/ ^task/$ [name='task-list']
   3. api/ ^task\.(?P<format>[a-z0-9]+)/?$ [name='task-list']
   4. api/ ^task/(?P<pk>[^/.]+)/$ [name='task-detail']
   5. api/ ^task/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='task-detail']
   6. api/ ^task/(?P<pk>[^/.]+)/change_state/$ [name='task-change-state']
   7. api/ ^task/(?P<pk>[^/.]+)/change_state\.(?P<format>[a-z0-9]+)/?$ [name='task-change-state']
   8. api/ ^task/(?P<pk>[^/.]+)/edit_description/$ [name='task-edit-description']
   9. api/ ^task/(?P<pk>[^/.]+)/edit_description\.(?P<format>[a-z0-9]+)/?$ [name='task-edit-description']
   10. api/ ^task/(?P<pk>[^/.]+)/edit_title/$ [name='task-edit-title']
   11. api/ ^task/(?P<pk>[^/.]+)/edit_title\.(?P<format>[a-z0-9]+)/?$ [name='task-edit-title']
   12. api/ ^task/(?P<pk>[^/.]+)/link_tasks/$ [name='task-link-tasks']
   13. api/ ^task/(?P<pk>[^/.]+)/link_tasks\.(?P<format>[a-z0-9]+)/?$ [name='task-link-tasks']
   14. api/ ^$ [name='api-root']
   15. api/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
```

---