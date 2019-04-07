import mysql.connector
cnx = mysql.connector.connect(
    user='root', password='unvisible777', host='127.0.0.1', database='employees')
cursor=cnx.cursor()
salaries = [(1,1,4,235),
            (2,2,7,655),
            (3,3,8,256),
            (4,4,2,365),
            (5,5,1,460),
            (6,6,3,450),
            (7,7,5,310),
            (8,8,6,700),
            (9,9,12,997)]

adding_salaries="""INSERT INTO salary (No, EmpNo, Month, Net)
                   VALUES (%s, %s, %s, %s)"""
result = cursor.executemany(adding_salaries,salaries)
cnx.commit()
cnx.close()