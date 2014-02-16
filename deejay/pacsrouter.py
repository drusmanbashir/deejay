class pacsRouter(object):

        def db_for_read(self, model, **hints):
                if model._meta.app_label == 'pacsCon':
                        return 'pacs'                   # confusing but this is also the name of the second database as well as an appname
                return None

        def db_for_write(self, model, **hints):
            if model._meta.app_label == 'pacsCon':
                return 'pacs'
            return None

        def allow_relation(self, obj1, obj2, **hints):
            if obj1._meta.app_label == 'pacsCon' or \
                    obj2._meta.app_label == 'pacsCon':
                        return True
            return None

        def allow_syncdb(self, db, model):
            if db == 'pacs' or model._meta.app_label == 'pacsCon':
                #return False
                return True
            else:
                return True
