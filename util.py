def genUUID():
    import uuid
    return str(uuid.uuid1())

def today():
     import datetime
     n = datetime.datetime.now().strftime('%Y%m%d')
     return n

def now():
    import datetime
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
