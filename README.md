#{{ project_name|title }}
{% if False %}

## Starting a project

django-admin.py startproject --template=https://github.com/brandonvfx/django-project-template/zipball/master --extension=py,md <project_name>

{% endif %}
## Virutal Env setup
mkvirtualenv {{ project_name }} 

pip install -r $PWD/requirements/dev.pip

echo "export DJANGO_SETTINGS_MODULE={{ project_name }}.conf.local.settings" >> $VIRTUAL_ENV/bin/postactivate

echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

## DB setup
python manage.py syncdb

python manage.py migrate

## Dev server
python manage.py runserver

