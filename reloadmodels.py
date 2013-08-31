# Desc: Imports the module with the name passed in, or imports it for first
#       time if it hasn't already been imported.
#
#       Purpose of this script is to speed up development of functions that
#       are written in an external editor then tested in IPython.
#
#       Without this script you have to exit & reenter IPython then redo
#       import statements, definitions of local variables, etc.
#
#       Note: doesn't work for Django models files, because Django caches
#       them in a structure called AppCache.
#
# Args: module to reload (string)

import sys

module_to_reload = sys.argv[1]

# Attempt to pop module
try:
    sys.modules.pop(module_to_reload)
    print 'reimporting...'
except KeyError:
    print 'importing for first time...'

# (re)import module
import_str = 'from {0} import *'.format(module_to_reload)
exec(import_str)
