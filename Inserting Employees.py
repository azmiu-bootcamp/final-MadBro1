import mysql.connector
cnx = mysql.connector.connect(
    user='root', password='unvisible777', host='127.0.0.1', database='employees')

cursor = cnx.cursor()
employees=[(1,'Aslan','Rustamov',19),
           (2,'Aysel','Hasanova',23),
           (3,'Kamran','Safarov',24),
           (4,'Rustam','Nagiyev',18),
           (5,'Nargiz','Aliyeva',19),
           (6,'Kamil','Aliyev',16),
           (7,'Nazim','Nebiyev',42),
           (8,'Maya','Lemanova',29),
           (9,'Teymur','Aslanov',21)]

adding_employees="""INSERT INTO employee (No, Name, Surname, Age)
        VALUES (%s, %s, %s, %s)"""
result = cursor.executemany(adding_employees,employees)
cnx.commit()
cnx.close()