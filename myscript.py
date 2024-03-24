import os

os.system("git bisect start f03308c e4cfc6f")
os.system("git bisect run python manage.py test")
