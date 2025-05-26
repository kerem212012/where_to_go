# WHERE TO GO
### How Need?
You don't know where you can go here with this map you can read descriptions about some places.
### How Run?
Play this code:
```pip install -r requirements.txt```
create file ```.env```
and write :
```python
SECRET_KEY = secretkey
ALLOWED_HOSTS = ["*",]
DEBUG = True
```
then play server:
```python
python manage.py runserver
```
### All Steps:
#### Step 1
- ```django-admin.exe startproject mysite .```
for new app.
#### Step 2
- ```pip install django```
- in ```views.py``` create func and return something
- import func from ```view.py```
- in ```urls.py urlpatterns``` add ```path('', func),```
- **for more read [click here](https://dvmn.org/encyclopedia/django/how-to-add-page/)**

#### Step 3

- download or make frontend you can [click here](https://github.com/devmanorg/where-to-go-frontend/)
- near static url paste this:
```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```
- in urls.py after ```urlpatterns = [...]``` add this:
```
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### Step 4
- add app ```python manage.py startapp name```
- in ```settings.py INSTALLED_APPS``` add:
```
'name.apps.NameConfig',
```
#### Step 5

- add model
- add fields in your model
- create superuser:```python manage.py createsuperuser```
- add model to admin

#### Step 6

- add model for image
- and connect with other

#### Step 7

- add in settings.py this:
```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

#### Step 8

- Move data from template to view

#### Step 9

- make views take data from db

#### Step 10

- make for all locations own site(only name)

#### Step 11

- now you need make it like json file

#### Step 12

- make sure every thing is good

#### Step 13

- add inlines to model in admin

#### Step 14

- use readonly_fields in admin
- [CookBook](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/imagefield.html)

#### Step 15

- remove image number

#### Step 16

- add django-tinymce [tutorial](https://github.com/jazzband/django-tinymce) for redactor

#### Step 17

- add .env with [click here](https://pypi.org/project/environs/)

#### Step 18

- publish to GitHub

#### Step 19

- deploy project to [pythonanywhere](https://www.pythonanywhere.com/)
- for venv and .env [click here](https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/)
- test [click here](https://gist.github.com/dvmn-tasks/f4a201547ae5f472771505df1d531a8d)

### PLS SUB
[Chipsinka](https://www.youtube.com/@Cipsinkagame/featured)
