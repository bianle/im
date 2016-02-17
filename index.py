# -*- coding: utf-8 -*-
import web
from orm import *
from util import *

urls = (
    '/login','login',
    '/send','send',
    '/receive','receive'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

class login:
    def GET(self):
        return "登录"

class send:
    def POST(self):
        ipt = web.input()
        m = Msg(id = genUUID(),sender=ipt.sender,msg= ipt.msg,timestamp = now())
        m.save()
        return "success"
class receive:
    def POST(self):
        ipt = web.input()
        sender = ipt.sender
        ts = ''
        rst = Visit.find(what="lastvisit",where="sender='"+sender+"'")
        try:
            ts = rst[0].LASTVISIT
        except:
            pass
        n = now()
        rst = Msg.find(what = "id,sender,msg,timestamp", where="timestamp>'"+ts+"'")
        msg = ''
        for rcd in rst:
            msg += rcd.SENDER+"["+rcd.TIMESTAMP+"]:\n"+rcd.MSG
            msg += '\n'
        a = Visit.execute("update im_visit set lastvisit = '"+n+"' where sender = '"+sender+"'" )
        if a==0:
            v = Visit(sender=sender,lastvisit=n)
            v.save()
        return msg
