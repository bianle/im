# -*- coding: utf-8 -*-
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import web
def getDb():
    db = 'im.db'   
    try:
        import sae.const

        db = sae.const.MYSQL_DB      # 数据库名
        user = sae.const.MYSQL_USER    # 用户名
        pw = sae.const.MYSQL_PASS    # 密码
        host = sae.const.MYSQL_HOST    # 主库域名（可读写）
        port = int(sae.const.MYSQL_PORT)    # 端口，类型为<type 'str'>，请根据框架要求自行转换为int
        #sae.const.MYSQL_HOST_S  # 从库域名（只读）
    except ImportError:
        pass
    return web.database(dbn='sqlite',db=db,)
def test():
    msg = ''
    db = getDb()
    db.insert('test',id=1,name='testestestestsetest')
    li = db.query('select id,name from test ')
    for rcd in li:
        msg+= '|'+bytes(rcd.id) +'|'+ bytes(rcd.name)+'|\n'
    id = 1
    db.update('test', name='test' ,where='id=$id' ,vars=locals())
    li = db.select('test',what='id,name,id as idd')
    for rcd in li:
        msg+= '|'+bytes(rcd.id) +'|'+ rcd.name+'|'+bytes(rcd.idd)+'|\n'
    db.delete('test', where = 'id = $id', vars = locals())
    return msg;
if __name__ == "__main__":
    db = getDb()
    db.insert('test',id=1,name='testestestestsetest')
    li = db.query('select id,name from test ')
    for rcd in li:
        print '|'+bytes(rcd.id) +'|'+ rcd.name+'|'
    id = 1
    db.update('test', name='test' ,where='id=$id' ,vars=locals())
    li = db.select('test',what='id,name,id as idd')
    for rcd in li:
        print '|'+bytes(rcd.id) +'|'+ rcd.name+'|'+bytes(rcd.idd)
    db.delete('test', where = 'id = $id', vars = locals())
