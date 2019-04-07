import mysql.connector
cnx = mysql.connector.connect(
    user='root', password='unvisible777', host='127.0.0.1', database='employees')
cursor = cnx.cursor()

print("1: Ən çox maaş alan işçi")
print("2: Ən az maaş alan işçi ")
print("3: Bütün işçilərin adları və maaşları")
choice=int(input("Prosesslərdən birini seçin: "))

if choice==1:
    cursor.execute("""select employee.Name, employee.Surname, salary.Net from salary 
        inner join employee
        on salary.EmpNo=employee.No order by Net desc""")
    for o in cursor:
        print(o)
        break
    
if choice==2:
    cursor.execute("""select employee.Name, employee.Surname, salary.Net from salary 
        inner join employee
        on salary.EmpNo=employee.No order by Net asc""")
    for o in cursor:
        print(o)
        break   
    
if choice==3:
    cursor.execute("""select employee.Name, salary.Net from salary 
        inner join employee
        on salary.EmpNo=employee.No""")
    for o in cursor:
        print(o)
