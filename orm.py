# -*- coding: utf-8 -*-
from copy import copy
from sqlite import getDb
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
    
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
        
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print ('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        if not attrs.has_key('__table__'):
            attrs['__table__'] = name # 
        attrs['__mappings__'] = mappings # 
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
    
    def modify(self,**kwargs):
        params = copy(self)
        try:
            params['where'] = kwargs['where']
            params['vars'] = kwargs['vars']
        except:
            params['where']='id='+str(self.id)
        getDb().update(self.__table__,**params)
    def remove(self):
        getDb().delete(self.__table__,where="id="+self.id)
        print 'remove'

    
    
    def save(self):
        it = getDb().insert(self.__table__,**self)
        setattr(self, 'id', it)
        return it
    
    @classmethod   
    def find(cls,**kwargs):
        rs = getDb().select(cls.__table__,**kwargs)
        return rs
    
    @classmethod
    def execute(cls,sql,**kwargs):
        rs = getDb().query(sql,**kwargs)
        '''
        if(isinstance(rs, long)):
            return rs
        else:
            
            for rcd in rs:
                rcd = dict(rcd)
                lst.append(rcd)
            return lst
        '''
        return rs
    
    

class Msg(Model):
    ''
    __table__ = 'IM_MSG'
    id = StringField('ID')
    sender = StringField('SENDER')
    msg = StringField('MSG')
    timestamp = StringField('TIMESTAMP')

class Visit(Model):
    ''
    __table__ = 'IM_VISIT'
    sender = StringField('SENDER')
    lastvisit = StringField('LASTVISIT')
    
if __name__ == '__main__':
    #q = Question(id='3',title=u"测试2",desc=u'测试测试测试')
    ##q.save()
    ##Question(id='2').remove()
    #print q.title
    #print type(q.title)
    #print 'success'
    print 111
    qi = Order(id = 1)
    qi.save()
    print '----------'
