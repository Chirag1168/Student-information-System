import MySQLdb
def test():
    db=MySQLdb.connect("localhost","root","123456","student")
    cursor=db.cursor()
    sql="select * from stu"
    try:
        cursor.excute(sql)
        results=cursor.fetchall()
        for row in results:
            en=row[0]
            nm=row[1]
            j=row[2]
            s=row[3]
            print "rollno=%d,name=%s,stream=%s,marks=%d" %(en,nm,j,s)
    except:
        print "error"
    db.close()
