import pymysql

servername="localhost"
username="root"
password=""
dbname="school"

print
print("1.Create A Record")
print("2.Edit A Record")
print("3.View A Record")
print("4.Delete A Record")
print("5.Exit")
ch=int(input("Please Enter your choice:"))

if ch==1:
	name=input("Enter student name:")
	rno=int(input("Enter student roll number:"))
	per=float(input("Enter percentage of student:"))
	try:
		db=pymysql.connect(servername,username,password,dbname)
		query="insert into student(name,rno,per) values('{}','{}','{}')".format(name,rno,per)
		c=db.cursor()
		try:
			c.execute(query)
			print("Record inserted successfully.....")
			db.commit()
		except Exception:
			db.rollback()
			print("Falied to insert...")	

	except Exception:
		print("Failed to connect....")		

if ch==2:
		view_id=int(input("Please enter the id of the student to be updated:"))
		try:
			db=pymysql.connect(servername,username,password,dbname)
			
			query="select * from student where id={}".format(view_id)
			c=db.cursor()
			try:
				c.execute(query)
				res=c.fetchone()
				
				print("The existing details of student are:")
				print("Id:",res[0])
				print("Name:",res[1])
				print("Roll Number:",res[2])
				print("Percentage:",res[3])
				print()
				print("1.To update the name of student")
				print("2.To update the roll number of student")
				print("3.To update the percentage of student")
				ch2=int(input("Please enter your choice:"))
				if ch2==1:
					update_name=input("Please enter name to be updated:")
					try:
						
						query1="update student set name='{}' where id={}".format(update_name,view_id)
						c1=db.cursor()
						c1.execute(query1)
						db.commit()
						print("Record updated successfully.")
					except Exception:
						db.rollback()
						print("Failed to update the record")

				if ch2==2:
					update_rno=input("Please enter roll number to be updated:")
					try:
						
						query1="update student set rno='{}' where id={}".format(update_rno,view_id)
						c1=db.cursor()
						c1.execute(query1)
						db.commit()
						print("Record updated successfully.")
					except Exception:
						db.rollback()
						print("Failed to update the record")

				if ch2==3:
					update_per=input("Please enter percentage to be updated:")
					try:
						
						query1="update student set per='{}' where id={}".format(update_per,view_id)
						c1=db.cursor()
						c1.execute(query1)
						db.commit()
						print("Record updated successfully.")
					except Exception:
						db.rollback()
						print("Failed to update the record")					

			except Exception:
				print("Failed to view the records as the id number don't exist.")

			
		except Exception:
			print("Failed to connect.")
		

if ch==3:
	print("1.To view record of every student")
	print("2.To view record of particular student")
	ch1=int(input("Please enter your choice:"))
	if ch1==1:
		try:
			db=pymysql.connect(servername,username,password,dbname)
			
			query="select * from student"
			c=db.cursor()
			try:
				c.execute(query)
				res=c.fetchall()
				for x in res:
					print("Student details.....")
					print("Id:",x[0])
					print("Name:",x[1])
					print("Roll Number:",x[2])
					print("Percentage:",x[3])
					print()

			except Exception:
				print("Failed to view the records.")

		except Exception:
			print("Failed to connect.")				
	if ch1==2:
		view_id=int(input("Please enter the id of the student:"))
		try:
			db=pymysql.connect(servername,username,password,dbname)
			
			query="select * from student where id={}".format(view_id)
			c=db.cursor()
			try:
				c.execute(query)
				res=c.fetchone()
				
				print("Student details.....")
				print("Id:",res[0])
				print("Name:",res[1])
				print("Roll Number:",res[2])
				print("Percentage:",res[3])
				print()

			except Exception:
				print("Failed to view the records.")

		except Exception:
			print("Failed to connect.")

if ch==4:
	delete_id=input("Enter student id to be deleted:")
	
	try:
		db=pymysql.connect(servername,username,password,dbname)
		query="delete from student where id={}".format(delete_id)
		c=db.cursor()
		try:
			c.execute(query)
			print("Record deleted successfully.....")
			db.commit()
		except Exception:
			db.rollback()
			print("Falied to delete...")	

	except Exception:
		print("Failed to connect....")	

if ch==5:
	exit()
