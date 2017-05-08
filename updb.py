import MySQLdb
import sys, getopt
def connect_db():
    """Connect database and return db and cursor"""
    db = MySQLdb.connect(host="localhost",user='udfin',
                          passwd='udfin',db="bcmsa")
    cursor = db.cursor()
    return db, cursor
def update(sql):
    db, cursor = connect_db()
    try:
        #print ('begin update mysql ',sql)
        rt=cursor.execute(sql)
        #print ('rtn',rt)
        db.commit()
    except MySQLdb.Warning, w:
        sqlWarning =  "Warning:%s" % str(w)
        print sqlWarning
    except MySQLdb.Error, e:
        sqlError =  "Error:%s" % str(e)
        print sqlError
        db.rollback()
    except:
        db.rollback()
    db.close()
def useage():
    print 'updb -i '
    print '\t-i sql to run'
    return

def updatevalue(ownvalue):
    pass

opts, args = getopt.getopt(sys.argv[1:], "hi:o:u:")
for op, value in opts:
    if op == "-i":
        update(value)
        sys.exit()
    if op=="-u":
        updatevalue(value)
        sys.exit()
    elif op == "-h":
        useage()
        sys.exit()
