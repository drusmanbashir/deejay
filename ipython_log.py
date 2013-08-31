# IPython log file

case = Case.objects.get(pk=1)
case.folder
case.validate(
)
runlog ipython.log
get_ipython().magic(u'logstart ')
casi = Case.objects.get(pk=1)
casi.folder
casi.validate()
get_ipython().magic(u'logoff ')
