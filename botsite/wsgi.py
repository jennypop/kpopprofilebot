import os
import sys

path = os.path.expanduser('/home/kpopprofilebot/botsite')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'botsite.settings'
os.environ['DJANGO_SECRET_KEY'] = '(iba:V$o7*P""huxBKX}^l?^@_S.^sGF3D{!jrB_H*>KaG8rWO'
os.environ['DJANGO_ALLOWED_HOSTS']='<www.your-domain.com>'
os.environ['DJANGO_ADMIN_URL']='<not admin/>'
os.environ['MAILGUN_API_KEY']='<mailgun key>'
os.environ['MAILGUN_DOMAIN']='<mailgun sender domain (e.g. mg.yourdomain.com)>'
os.environ['DJANGO_AWS_ACCESS_KEY_ID']=
os.environ['DJANGO_AWS_SECRET_ACCESS_KEY']=
os.environ['DJANGO_AWS_STORAGE_BUCKET_NAME']=
os.environ['DATABASE_URL']='<see below>'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())