import mysql.connector
cnx = mysql.connector.connect(
    user='root', password='unvisible777', host='127.0.0.1', database='employees')
cursor = cnx.cursor()

cursor.execute("""CREATE TABLE employee ( No INT PRIMARY KEY AUTO_INCREMENT,
                Name VARCHAR(20) not null,Surname VARCHAR(20),Age int)""")

cursor.execute("""CREATE TABLE salary (No int, EmpNo integer,
                FOREIGN KEY(EmpNo) references employee(No),Month int, Net int)""")
