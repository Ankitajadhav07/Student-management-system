import mysql.connector

# Database Connection
dbconnection = mysql.connector.connect(
    user='root',
    password='Mysql',
    host='localhost',
    port=3306,
    database='python_1234'
)

# Cursor Object
mycursor = dbconnection.cursor()

# Create Table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS stud_info (
    id INT,
    name VARCHAR(30),
    city VARCHAR(20),
    institute_name VARCHAR(30),
    course_name VARCHAR(30)
)
""")
dbconnection.commit()

# Insert Function
def insert_record(id, name, city, institute_name, course_name):
    sql = "INSERT INTO stud_info (id, name, city, institute_name, course_name) VALUES (%s, %s, %s, %s, %s)"
    values = (id, name, city, institute_name, course_name)
    mycursor.execute(sql, values)
    dbconnection.commit()

# Display Function
def display_record():
    sql = "SELECT * FROM stud_info"
    mycursor.execute(sql)

    print("id\tname\tcity\tinstitute_name\tcourse_name")
    for row in mycursor.fetchall():
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")


def update_record(id,city):
    sql="update stud_info set city=%s where id=%s"
    values=(city,id)
    mycursor.execute(sql,values)
    dbconnection.commit()
    print("Record updated successfully")

def delete_record(id):
    sql="delete from stud_info where id=%s"
    values=(id,)
    mycursor.execute(sql,values)
    dbconnection.commit()
    print("Record deleted sucessfully")




# Main Menu
while True:
    print("""
1. Insert Records
2. Display Records
3. Update Records
4. Delete Records
5. Exit
""")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        city = input("Enter City: ")
        institute_name = input("Enter Institute Name: ")
        course_name = input("Enter Course Name: ")
        insert_record(id, name, city, institute_name, course_name)

    elif ch == 2:
        display_record()

    elif ch == 3:
        id=int(input("Enter id="))
        city=input("Enter city= ")
        update_record(id,city)

    elif ch == 4:
        id=int(input("Enter id="))
        delete_record(id)

    elif ch == 5:
        print("Exiting")
