gnome-terminal --tab -e "bash -c 'cd /home/manikandan/workspace/django/;source /home/manikandan/env/django/bin/activate; python manage.py runserver 0:8000;exec $SHELL'" --tab -e "bash -c 'cd /home/manikandan/workspace/new/django/;source /home/manikandan/env/django/bin/activate; python manage.py runserver 0:8001;exec $SHELL'"
