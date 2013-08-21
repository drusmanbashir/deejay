#!/home6/docsmart/python27/bin/python
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/home6/docsmart/python27")
sys.path.insert(13, "/home6/docsmart/main")

os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
