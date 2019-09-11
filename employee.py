import matplotlib.pyplot as plt
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="company")
mycursor=mydb.cursor()
cur=mydb.cursor()
j = k = 0
a = []
j = []
ch=''
def emp_sal():
    str = "select * from employee"
    mycursor.execute(str)
    ans = mycursor.fetchall()
    for i in ans:
        plt.bar(i[1], i[2], label=i[1])
    plt.title('Current Employee Salary')
    plt.xlabel('Name')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()

def emp_ind():
    a = []
    j = []
    id = int(input("Enter employee Id :"))
    qry = "select * from salary where id=%s"
    val = (id,)
    mycursor.execute(qry, val)
    ans = mycursor.fetchall()
    mydb.commit()
    for i in ans:
        a.append(i[3])
        j.append(i[2])
    plt.plot(a, j)
    plt.title('Salary Growth')
    plt.xlabel('year')
    plt.ylabel('salary')
    plt.show()

def emp_skill():
    a = []
    j = []
    id = int(input("Enter employee Id :"))
    qry = "select * from skill where id=%s"
    val = (id,)
    cur.execute(qry, val)
    ans = cur.fetchall()
    lang = 'html', 'php', 'python', 'java'
    for i in ans:
        a.append(i[2])
        a.append(i[3])
        a.append(i[4])
        a.append(i[5])
    figureObject, axesObject = plt.subplots()
    axesObject.pie(a, labels=lang, autopct='%1.2f%%', startangle=90, shadow=True, explode=(0.1, 0, 0, 0))
    plt.title('PieChart')
    axesObject.axis('equal')
    plt.legend()
    plt.show()

while ch != 4:
    print("1. Employee salary")
    print("2. Individual employee salary growth")
    print("3. Employee Skills")
    print("4. exit")
    ch=int(input("Enter Your choice:"))

    if ch == 1:
       emp_sal()
    elif ch == 2:
        emp_ind()
    elif ch == 3:
        emp_skill()
    elif ch == 4:
        exit(0)