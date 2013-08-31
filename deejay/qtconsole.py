#enable running django from ipython qtconsole command followed by importing this file
#remember to place this file in the same dir as settings.py
#after than cd to django root dir

import settings
import django.core.management
django.core.management.setup_environ(settings)
