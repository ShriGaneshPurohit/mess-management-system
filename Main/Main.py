import tkinter as tk                            #For GUI
from PIL import ImageTk							#For Images 
from tkinter import  ttk,messagebox					#For Info Box GUI
import mysql.connector as sql					#For Connecting DataBase With Project
import time as tm 								#For Displaying Time in Login Form
import os 									 	#For Deleting Image 
from datetime import datetime,date,timedelta

from tkcalendar import Calendar
from tkinter import *

#Linking database 
mycon = sql.connect(host = 'localhost',
	user = 'root',
	passwd = '0000'
	,database = 'messmanage',port=3306)	

cursor = mycon.cursor()
#_____________Imp Functions Declaration___
def admindash():pass

#_____________Login Function___________():
def Login_Func() :
	a=Username_Entry.get()
	b=Password_Entry.get()

#_____________Verfiying Wether The Entry are not null___
	if a =='' and b=='':
		tk.messagebox.showinfo("Empty Or No Info", "Please Enter User Name And Password")

	elif a =='' :
		tk.messagebox.showinfo("Empty Or No Info", "Please Enter User Name")
	elif b =='' :
		messagebox.showinfo("Empty Or No Info", "Please Enter Password")
	elif a =='' and b=='':
		messagebox.showinfo("Empty Or No Info", "Please Enter User Name And Password")
    
	elif a!='' and b!='':
		data = cursor.execute('select * from logdata')
		data2 = cursor.fetchall()
		flag = 0
		#__________________User Dashboard____________________________
		for row in data2 :
			if row[1] ==a and row[2] ==b:
				
				flag=1
				date_str = row[4]
				date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
				
				if(( row[3] == "U" or row[3] == "u") and date_object > date.today()):
					userdash()
					#print('Login Successfully')
				
				elif(row[3] =="A" or row[3] == "a"):
					admindash()
					#print('Login Successfully')

				elif(( row[3] == "U" or row[3] == "u") and date_object <= date.today()):
					messagebox.showerror("Renew Licence", "Contact 9404457569 To Renew Service")

							
		if flag == 0:
			messagebox.showerror("No Match", "Please Enter Correct Combination")

def clear() :
	Username_Entry.delete(0, 'end')	
	Password_Entry.delete(0, 'end')

#___________________________ADMIN DASH BOARD________________
def admindash():
	#Main.withdraw
	admin = tk.Toplevel(Main)
	admin.geometry('1024x550+250+100')
	admin.resizable(False,False)
	admin.configure(bg='#ffffff')
	userFrame =tk.LabelFrame(admin,font=('Verdana',18,'bold','italic'),
		fg='black',
		borderwidth=10,bg='#F2F2F5',padx=10,pady=5)
	userFrame.pack(fill='x')
	Heading = tk.Label(userFrame ,
		text = "Mess Management System\nAdmin Dashboard ",
		font= ('Helvetica',19,'bold','italic'),
		bg='#F2F2F5',fg='Black',bd=10).pack(fill='x')

#           Left Frame

	Frame_Buttons = tk.LabelFrame(admin,text=' Features ',font=('helvatica',14,'bold','italic'),
		fg='black',borderwidth=5,bg='#ffffff',padx=5,pady=5)
	Frame_Buttons.pack(anchor='w',padx=40,pady=6,fill='y')

	a=Username_Entry.get()
	b="Welcome "+a.capitalize()
	Add_label = tk.Label(admin,text=b ,bg='#ffffff',font=('helvatica',18,'bold'),fg='#67D8DA').place(x=400,y=125)

#                         Addding Buttons 

#Admin . Addbutton

	def addUser_Admin():
		window = tk.Toplevel(admin)
		window.geometry('410x365+570+240')
		window.config(bg="#FEFDEF")
		window.resizable(False,False)
		window.title("Add User")


		label_Heading = tk.Label(window,text='Add User Details',bg="#FEFDEF"
			,font=('Helvetica',16,"italic","bold")).pack(anchor='center',side='top',fill='x')
		Frame_Body  = tk.LabelFrame(window,text='Enter Details',font=('Helvetica',16,"italic")
			,borderwidth=4,bg='#FEFDEF',padx=10,pady=5)
		Frame_Body.pack(fill='x',pady=15)


		##DATA ELEMENTS FOR addUser_Admin

		##Uid
		uid_label = tk.Label(Frame_Body,text="User Id (INT)",bg='#FEFDEF',font=('Helvetica',14,"italic")).grid(row=0,column=0,sticky ="w")
		uid_Field = tk.Entry(Frame_Body,width=15,bd=1,font=('Verdana',13,'bold','italic'),fg='Purple')
		uid_Field.grid(row=0,column=1,padx=4,pady =2)
		
		
		##Uname
		
		Uname_label = tk.Label(Frame_Body,text="User Name",bg='#FEFDEF',font=('Helvetica',14,"italic")).grid(row=1,column=0,sticky ='w')
		Uname_Field = tk.Entry(Frame_Body,width=15,bd=1,font=('Verdana',13,'bold','italic'),fg='Purple')
		Uname_Field.grid(row=1,column=1,padx=4,pady =2)
		
		
		##Pass

			
		Pass_label = tk.Label(Frame_Body,text="User Password",bg='#FEFDEF',font=('Helvetica',14,"italic")).grid(row=2,column=0,sticky ='w')
		Pass_Field = tk.Entry(Frame_Body,width=15,bd=1,font=('Verdana',13,'bold','italic'),fg='Purple')
		Pass_Field.grid(row=2,column=1,padx=4,pady =2)
		
		##Rights

		Rights_label = tk.Label(Frame_Body,text="User Rights(A,U)",bg='#FEFDEF',font=('Helvetica',14,"italic")).grid(row=3,column=0,sticky ='w')
		Rights_Field = tk.Entry(Frame_Body,width=15,bd=1,font=('Verdana',13,'bold','italic'),fg='Purple')
		Rights_Field.grid(row=3,column=1,padx=4,pady =2)
		


		def add_Clear():
			uid_Field.delete(0, "end")
			Uname_Field.delete(0, "end")
			Pass_Field.delete(0, "end")
			Rights_Field.delete(0, "end")
			valCal_Field.delete(0, "end")
			valCal_Field.insert(0, "YYYY-MM-DD")
		##Validity


		def val_calender():
			valCal_Field.delete(0, "end")
			calWin = tk.Toplevel(window)
			calWin.title("Select Date")

			cal = Calendar(calWin, selectmode = 'day')

			cal.pack(pady = 20)


			def set_date():
				
				date_str =  (cal.get_date()).replace('/', '-')

				date_object = datetime.strptime(cal.get_date(),'%m/%d/%y').date()
				
				
				valCal_Field.insert(0,date_object)
				calWin.destroy()
			


			tk.Button(calWin, text = "Get Date",command = set_date).pack(pady = 20)
	

			calWin.mainloop()

		valCal_label = tk.Label(Frame_Body,text="Valid Till",bg='#FEFDEF',font=('Helvetica',14,"italic")).grid(row=4,column=0,sticky ='w')
		valCal_Field = tk.Entry(Frame_Body,width=15,bd=1,font=('Verdana',13,'bold','italic'),textvariable="YYYY-MM_DD",fg='Purple')
		valCal_Field.grid(row=4,column=1,padx=4,pady =2)
		valCal_Field.insert(0, "YYYY-MM-DD")
		add_Clear()
		##Clear Button
	
		Calender_Button = tk.Button(window,text='Select Date',height=1 ,bg="lavender",command=val_calender,borderwidth=0,).pack(fill='x' ,pady=2)

		
		addClear_Button = tk.Button(window,text='Clear Fields',height=2 ,bg="#F15B6C",command=add_Clear,borderwidth=0,).pack(fill='x' ,pady=5)

		def add_ok():
			try:
				query = "Insert Into logdata(uid,uname,upass,control,validity) values({},'{}','{}','{}','{}')".format(int(uid_Field.get()),Uname_Field.get(),
				Pass_Field.get(),Rights_Field.get(),valCal_Field.get())
				cursor.execute(query)
				mycon.commit()
				messagebox.showinfo("Add User", "User Added Succesfully",parent = window)

				#print("Inserted Succes")
				clear() 
			except:
				ans = messagebox.askretrycancel("Mismatch", "User already exist try other username",parent = window)
				if ans == True :
					clear()
				else:
					window.destroy()

		addOk_Button = tk.Button(window,text='Add User',height=2,bg="#60BE92",command=add_ok,borderwidth=0).pack(fill='x',pady=5)
		

		 

		window.mainloop()



	Add_img = ImageTk.PhotoImage(file ='H:/Mess/Assests/admin_dash_icons/add.png')
	Add_Button = tk.Button(Frame_Buttons,text='Add Students',command=addUser_Admin,image=Add_img,borderwidth=0,bg='#ffffff').pack(padx=1)
	Add_label = tk.Label(Frame_Buttons,text="Add Data",bg='#ffffff',font=('helvatica',12,'bold')).pack()

#Admin . Remove Button
	

	def admin_remove_user():
		window = tk.Toplevel(admin)
		window.geometry('450x400+570+240')
		window.config(bg="#FEFDEF")
		window.resizable(False,False)
		window.title("Add User")

		label_Heading = tk.Label(window,text='User Details',bg="#FEFDEF"
			,font=('Helvetica',16,"italic","bold")).pack(anchor='center',side='top',fill='x')
		Frame_Body  = tk.LabelFrame(window,text='User Info',font=('Helvetica',16,"italic")
			,borderwidth=4,bg='#FEFDEF',padx=10,pady=5)
		Frame_Body.pack(fill='x',pady=15)

		r_set1=cursor.execute("SELECT * from logdata") # collect all records 
		r_set = cursor.fetchall()
		l1=["UID","UNAMES","PASSWORD","RIGHTS","VALIDITY"] # List of column headers.

		# Using treeview widget
		trv_admin_remove_user = ttk.Treeview(Frame_Body, selectmode ='browse',columns=l1,
  		show='headings',height=10)
		trv_admin_remove_user.grid(row=1,column=1,padx=20,pady=20)

		# set columns and headings for Treeview 
		
		for i in l1:
			trv_admin_remove_user.column(i, anchor ='c', width=70)
			trv_admin_remove_user.heading(i, text =i)
		# Adding rows of data from MySQL student table to treeview 
		i= 0
		for row in r_set: 
			trv_admin_remove_user.insert("", 'end',iid=row[0], text=row[0],values =list(row))
			i+=1

		vs = ttk.Scrollbar(Frame_Body,orient="vertical", command=trv_admin_remove_user.yview)#V Scrollbar
		trv_admin_remove_user.configure(yscrollcommand=vs.set)  # connect to Treeview
		vs.grid(row=1,column=2,sticky='ns')


		def remove_one():
			msg_box = tk.messagebox.askquestion('Remove User', 'Are you sure you delete user?',icon='warning',parent = window)
			
			if msg_box == 'yes':
				x = trv_admin_remove_user.selection()[0]
				cursor.execute("DELETE from logdata WHERE uid=" +x[0])
				mycon.commit()
				trv_admin_remove_user.delete(x)
				tk.messagebox.showinfo('Remove User', 'Delete sucessful',parent = window)

			else:
				pass        		


############## Admin Rmove Button

		remove_one_button = tk.Button(window, text="Remove One Selected", command=remove_one).pack(fill='x')



		window.mainloop()


	Remove_img = ImageTk.PhotoImage(file ='H:/Mess/Assests/admin_dash_icons/remove.png')
	Remove_Button = tk.Button(Frame_Buttons,image=Remove_img,borderwidth=0,bg='#ffffff',command=admin_remove_user).pack()
	Remove_label = tk.Label(Frame_Buttons,text="Remove User",bg='#ffffff',font=('helvatica',12,'bold')).pack()



#Admin . Showbutton

	def admin_show_users():
		window = tk.Toplevel(admin)
		window.geometry('430x365+570+240')
		window.config(bg="#FEFDEF")
		window.resizable(False,False)
		window.title("Add User")

		label_Heading = tk.Label(window,text='User Details',bg="#FEFDEF"
			,font=('Helvetica',16,"italic","bold")).pack(anchor='center',side='top',fill='x')
		Frame_Body  = tk.LabelFrame(window,text='User Info',font=('Helvetica',16,"italic")
			,borderwidth=4,bg='#FEFDEF',padx=10,pady=5)
		Frame_Body.pack(fill='x',pady=15)

		r_set1=cursor.execute("SELECT * from logdata") # collect all records 
		r_set = cursor.fetchall()
		l1=["UID","UNAMES","PASSWORD","RIGHTS","VALIDITY"] # List of column headers.

		# Using treeview widget
		trv_admin_show_users = ttk.Treeview(Frame_Body, selectmode ='browse',columns=l1,
  		show='headings',height=10)
		trv_admin_show_users.grid(row=1,column=1,padx=20,pady=20)

		# set columns and headings for Treeview 
		
		for i in l1:
			trv_admin_show_users.column(i, anchor ='c', width=70)
			trv_admin_show_users.heading(i, text =i)
		# Adding rows of data from MySQL student table to treeview 
		i= 0
		for row in r_set: 
			trv_admin_show_users.insert("", 'end',iid=row[0], text=row[0],values =list(row))
			i+=1

		vs = ttk.Scrollbar(Frame_Body,orient="vertical", command=trv_admin_show_users.yview)#V Scrollbar
		trv_admin_show_users.configure(yscrollcommand=vs.set)  # connect to Treeview
		vs.grid(row=1,column=2,sticky='ns')

		


		window.mainloop()



	Show_img = ImageTk.PhotoImage(file ='H:/Mess/Assests/admin_dash_icons/show.png')
	Show_Button = tk.Button(Frame_Buttons,text='Show Users',command=admin_show_users,image=Show_img,borderwidth=0,bg='#ffffff').pack(padx=1)
	Show_label = tk.Label(Frame_Buttons,text="Show Users",bg='#ffffff',font=('helvatica',12,'bold')).pack()

#           Right Frame

	RFrame_Buttons = tk.LabelFrame(admin,text=' Features ',font=('helvatica',14,'bold','italic'),
		fg='black',borderwidth=5,bg='#ffffff',padx=5,pady=5)
	RFrame_Buttons.place(x=865,y=115,)
	#print("Rframe")

	def on_closing():
		if messagebox.askokcancel("Logout", "Click on ok to logout.",parent=admin):
			admin.destroy()

#Admin . Logout
	logout_img = ImageTk.PhotoImage(file ='H:/Mess/Assests/admin_dash_icons/logout.png')
	logout_Button = tk.Button(RFrame_Buttons,text='Logout',command=on_closing,image=logout_img,borderwidth=0,bg='#ffffff').pack(padx=1)
	logout_label = tk.Label(RFrame_Buttons,text="logout",bg='#ffffff',font=('helvatica',12,'bold')).pack()


	admin.protocol("WM_DELETE_WINDOW", on_closing)

	admin.mainloop()

def userdash():
#_________________Student Master________________________	


	#________________DATABSE Functions__________________
	def State_card_databas():

		qurey = cursor.execute("select id,card_validity,cardstatus from student_data")
		data_row = list(cursor.fetchall())

		


		update_validdate_list = {}
		length1=len(data_row)
		#print(data_row)



		

		for row in data_row:
			j=0

			
			uid = row[0]
			date_object = row[1]

			if date_object == None:
				update_validdate_list[uid]="Pause"
				continue
				
			
			#Active
			if date_object >= date.today():
				update_validdate_list[uid]="Active"


			#Active
			elif date_object < date.today():
				update_validdate_list[uid]="Expired"
			
			
			else:
				pass
			j +=1


		#print(update_validdate_list)
		#print(data_row)

		
		for dict_1 in update_validdate_list:
			#print(dict_1)
			#print(type(dict_1))
			#print(type(update_validdate_list.get(dict)))

			qurey = "UPDATE student_data SET cardstatus = '{}' where id ={}".format(update_validdate_list.get(dict_1),dict_1)
			cursor.execute(qurey)
			mycon.commit()
		
		
	State_card_databas()
	

	def student_master():

		window = tk.Toplevel(User_Window)
		window.title('Student Master')
		window.geometry('1024x550+250+100')
		window.resizable('false','false')
		window.focus()


		#Tree Frame body
		Memeber_Frame  = tk.LabelFrame(window,text='Members Record',font=('Helvetica',16,"italic")
					,borderwidth=3.5,padx=10,pady=5)
		Memeber_Frame.pack(fill='x',pady=15)

		#TreeView Scrollbar
		tree_scroll = ttk.Scrollbar(Memeber_Frame)
		tree_scroll.pack(side="right",fill="y")

		
		
		# Using treeview widget

		l1=["CARD NO","NAMES","BRANCH","PHONE NO","CITY","CARD VALIDITY","DAYS LEFT","MEALS OPTED FOR"] # List of column headers.

		trv = ttk.Treeview(Memeber_Frame, selectmode ='browse',columns=l1,

		#set columns and headings for Treeview		   
		show='headings',height=10,)
		
		trv.pack(pady=20)

		def refresh():
			State_card_databas()
			for item in trv.get_children():
				trv.delete(item)


			r_set1=cursor.execute("SELECT * from student_data") # collect all records 
			r_set = cursor.fetchall()		
				
	

		# Adding rows of data from MySQL student table to treeview 
			count= 0          
			for record in r_set:
				if record[8] == "Active":
					trv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('A',))
				elif record[8] == "Pause":
					trv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('P',))
				elif record[8] == "Expired":
					trv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('E',))
				else:
					trv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('D',))

				# increment counter
				count += 1
	
		


		
	
			for i in l1:
				if(i == "MEALS OPTED FOR"):
					trv.column(i, anchor ='c', width=150)
					trv.heading(i, text =i)
				else:
					trv.column(i, anchor ='c', width=117)
					trv.heading(i, text =i)
			
			
		
			
				
	

		refresh()
		

		def select_record(e):
			
			CardNo_Field.delete(0,"end")
			Name_Field.delete(0,"end")
			Branch_Field.delete(0, "end")
			Phone_Field.delete(0, "end")
			City_Field.delete(0, "end")
			Card_Validity_Entry.delete(0, "end")
			Days_left_Field.delete(0, "end")
			

			select_record = trv.focus()
			#grab record values
			values = trv.item(select_record,'values')
			#output

			CardNo_Field.insert(0, values[0]) 
			Name_Field.insert(0, values[1])
			Branch_Field.insert(0, values[2])
			Phone_Field.insert(0, values[3])
			City_Field.insert(0, values[4])
			Card_Validity_Entry.insert(0, values[5])
			Days_left_Field.insert(0, values[6])
			Meal_var.set(values[7])
			
						
	
					
					
				




		
		#_____________________________________________________________________________________________________________________________________________________
		#Record frame
		#Frame Body 
		Record_Frame  = tk.LabelFrame(window,text='Record',font=('Helvetica',9,"bold")
					,borderwidth=3.5,padx=10,pady=5)
		Record_Frame.pack(fill='x',pady=5)

		#__Labels
		CardNo_label = tk.Label(Record_Frame,text="Card No",font=('Helvetica',10,"bold")).grid(row=0,column=0,sticky ='e',padx=0)
		CardNo_Field = tk.Entry(Record_Frame,width=15,bd=1,font=('Verdana',10,))
		CardNo_Field.grid(row=0,column=1,sticky ='e',padx=5)

		Name_label = tk.Label(Record_Frame,text="Name",font=('Helvetica',10,"bold")).grid(row=0,column=2,sticky ='e')
		Name_Field = tk.Entry(Record_Frame,width=15,bd=1,font=('Verdana',10,))
		Name_Field.grid(row=0,column=3,sticky ='e',padx=5)

		Branch_label = tk.Label(Record_Frame,text="Branch",font=('Helvetica',10,"bold")).grid(row=0,column=4,sticky ='e')
		Branch_Field = tk.Entry(Record_Frame,width=15,bd=1,font=('Verdana',10,))
		Branch_Field.grid(row=0,column=5,sticky ='e',padx=5)

		Phone_label = tk.Label(Record_Frame,text="Phone",font=('Helvetica',10,"bold")).grid(row=0,column=6,sticky ='e')
		Phone_Field = tk.Entry(Record_Frame,width=15,bd=1,font=('Verdana',10,))
		Phone_Field.grid(row=0,column=7,sticky ='e',padx=7)

		City_label = tk.Label(Record_Frame,text="City",font=('Helvetica',10,"bold")).grid(row=0,column=8,sticky ='e')
		City_Field = tk.Entry(Record_Frame,width=15,bd=1,font=('Verdana',10,))
		City_Field.grid(row=0,column=9,sticky ='e',padx=5)



		def calender():
			Card_Validity_Entry.delete(0, "end")
			Days_left_Field.delete(0, "end")
			calWin = tk.Toplevel()
			calWin.title("Select Date")

			cal = Calendar(calWin, selectmode = 'day')

			cal.pack(pady = 20)

			def set_date():

				date_str =  (cal.get_date()).replace('/', '-')
				date_object = datetime.strptime(cal.get_date(),'%m/%d/%y').date()			

				Days_left_Field.insert(0,(date_object- date.today()).days)

				Card_Validity_Entry.insert(0,date_object)
				calWin.destroy()
			


			tk.Button(calWin, text = "Get Date",command = set_date).pack(pady = 20)
	

			calWin.mainloop()
			


		#0,1,2
		Card_Validity_label = tk.Label(Record_Frame,text="Card Validity",font=('Helvetica',10,"bold")).grid(row=1,column=0,sticky ='e')
		Card_Validity_Entry = tk.Entry(Record_Frame,width=15,bd=1,font=('Verdana',10,))
		Card_Validity_Entry.grid(row=1,column=1,sticky ='e',padx=5,pady = 3)
		
		Date_Select_btn = tk.Button(Record_Frame,text="Select Date",command=calender).grid(row=1,column=2,sticky ='w',padx=5,pady = 4)


		#3,4
		Days_Left_label = tk.Label(Record_Frame,text=" Days Left",font=('Helvetica',10,"bold")).grid(row=1,column=3,sticky ='w',columnspan=1)
		Days_left_Field = tk.Entry(Record_Frame,width=4,bd=1,font=('Verdana',10,),)
		Days_left_Field.grid(row=1,column=3,sticky ='e',padx=5,pady = 3)



		#5,6,7,8
		Meals_label = tk.Label(Record_Frame,text="     Meals",font=('Helvetica',10,"bold")).grid(row=1,column=4,sticky ='w',columnspan=1)
		
		Meal_Type = ["0. Select Meal","1. Breakfast Only","2. Lunch Only","3. Dinner Only","4. Breakfast + Lunch","5. Breakfast + Dinner","6. Lunch + Dinner ","7. Breakfast + Lunch + Dinner"]


		
		global Meal_var
		Meal_var = StringVar()
		Meal_var.set(Meal_Type[0])
		Meals_drop = ttk.OptionMenu(Record_Frame,Meal_var,*Meal_Type,)
		Meals_drop.place(y=27,x= 500)
		



		#_____________________________________________________________________________________________________________________________________________________
		#Commands frame
		#Frame Body 
		Command_Frame  = tk.LabelFrame(window,text='Commands',font=('Helvetica',9,"bold")
					,borderwidth=3.5,padx=10,pady=5)
		Command_Frame.pack(fill='x',pady=15)

		# Commands Button
		def update_query():
				try:
					
					date_object = datetime.strptime(Card_Validity_Entry.get(), '%Y-%m-%d').date()
					if(type(date_object) == type(date.today())):
						remove_selected()					
						add_query()
					else:
						messagebox.showwarning(title="Wrong Input", message="Enter a valid date.", parent = window)
				except:
					messagebox.showwarning(title="Missing Field", message="One or more field missing", parent = window)
					

			
	
		update_query_btn = tk.Button(Command_Frame,text="Update Record",width = 21,command=update_query).grid(row=0,column=0,sticky ='w',padx=5,pady = 4)

		def add_query():
			try:						
				if messagebox.askokcancel("Update", "Data will be added if clicked ok.",parent=window):

					global meal_id
					meal_id = Meal_var.get()[0]
					add_data = (CardNo_Field.get(),
					Name_Field.get(),
					Branch_Field.get(),
					Phone_Field.get(),
					City_Field.get(),
					Card_Validity_Entry.get(),
					Days_left_Field.get(),
					Meal_var.get(),meal_id)
					
						

					query = "INSERT INTO student_data(id ,sname ,Branch,Phone_No,city ,Card_Validity,days_left ,meals_opted ,cardStatus )VALUES({},'{}','{}','{}','{}','{}',{},'{}','{}')".format(add_data[0],add_data[1],add_data[2],add_data[3],add_data[4],add_data[5],add_data[6],add_data[7],'-',meal_id)
					cursor.execute(query)
					mycon.commit()
					query =  "UPDATE student_data SET Meal_identity = left(meals_opted,1)"
					cursor.execute(query)
					mycon.commit()
					
					refresh()

			except:
				messagebox.showwarning(title="Missing field or data exists", message="One or more field missing\nOr data already exists.", parent = window)

			

		add_query_btn = tk.Button(Command_Frame,text="Add Record",width = 21,command=add_query).grid(row=0,column=1,sticky ='w',padx=5,pady = 4)

		def remove_selected():
			try:
				if messagebox.askokcancel("Update", "Data will be removed if clicked ok.",parent=window):

					query = "Delete from student_data where id = {}".format(CardNo_Field.get())
					cursor.execute(query)
					mycon.commit()
					
					refresh()
			except:
					messagebox.showwarning(title="Missing Field", message="One or more field missing", parent = window)

					
			

		remove_selected_btn = tk.Button(Command_Frame,text="Remove Record",width = 21,command=remove_selected).grid(row=0,column=2,sticky ='w',padx=5,pady = 4)

		def clear_entry():
			
			CardNo_Field.delete(0,"end")
			Name_Field.delete(0,"end")
			Branch_Field.delete(0, "end")
			Phone_Field.delete(0, "end")
			City_Field.delete(0, "end")
			Card_Validity_Entry.delete(0, "end")
			Days_left_Field.delete(0, "end")
			Meal_var.set(Meal_Type[0])

			

		clear_entry_btn = tk.Button(Command_Frame,text="Clear Entry",width = 21,command=clear_entry).grid(row=0,column=3,sticky ='w',padx=5,pady = 4)

		def search_records():
			lookup_record = search_entry.get()
			# close the search box
			search.destroy()
			
			# Clear the Treeview
			for record in trv.get_children():
				trv.delete(record)
			
			

			cursor.execute("SELECT * FROM student_data WHERE id = {}".format(lookup_record))
			records = cursor.fetchall()
			
			# Add our data to the screen
			global count
			count = 0
			
			#for record in records:
			#	print(record)


			count= 0          
			for record in records:
				if record[8] == "Active":
					trv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('A',))
				elif record[8] == "Pause":
					trv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('P',))
				elif record[8] == "Expired":
					trv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('E',))
				else:
					trv.insert(parent='', index='end', iid=count, text='', values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('D',))

				# increment counter
				count += 1
	




		def lookup_records():
			global search_entry, search

			search = Toplevel(window)
			search.title("Lookup Records")
			search.geometry("350x200+571+200")
			search.focus()
			search.resizable(False,False)

			
			
			# Create label frame
			search_frame = LabelFrame(search, text="Card Number")
			search_frame.pack(padx=10, pady=10)

			# Add entry box
			
			search_entry = Entry(search_frame, font=("Helvetica", 18))
			search_entry.pack(pady=20, padx=20)

			# Add button
			search_button = Button(search, text="Search Records",width = 21,command=search_records)
			search_button.pack(padx=20, pady=20)
			
			devloper_Label =  tk.Label(search,text="© Developer By ShreeGanesh ☎ :- 9404457569   ",font=('Helvetica',10,"bold")).pack(fill="x",anchor='s')


			#Bind
			def search_Bind_fun(e):
				search.focus()
				search_entry.focus_set()
				if(search_entry.get() == ""):
					print("Try Again!!!")
				else:
					search_records()
				

			search.bind("<Return>",search_Bind_fun )


		search_btn = tk.Button(Command_Frame,text="Search Entry",width = 21,command=lookup_records).grid(row=0,column=4,sticky ='w',padx=5,pady = 4)

		refresh_btn = tk.Button(Command_Frame,text="Refresh ",width = 21,command=refresh).grid(row=0,column=5,sticky ='w',padx=5,pady = 4)



		#def add-record():
			#ALTER TABLE student_data ORDER BY id ASC;


		



		# bind the tree
		trv.bind("<ButtonRelease-1>",select_record)
		
		trv.tag_configure("A",background ="#D1EA2C")
		trv.tag_configure("P",background ="#F9BC02")
		trv.tag_configure("E",background ="#FD5308")
		trv.tag_configure("D",background ="")

		
		devloper_Label =  tk.Label(window,text="© Developer By ShreeGanesh ☎ :- 9404457569   ",font=('Helvetica',10,"bold")).pack(padx=10)
		
		#___COLOUR DESCRIPTION_
		Active_Label =  tk.Label(window,text="Active",font=('Helvetica',10,"bold"),bg="#D1EA2C").place(x=850,y=0)
		Paues_Label =  tk.Label(window,text="Pause",font=('Helvetica',10,"bold"),bg="#F9BC02").place(x=900,y=0)
		Expired_Label =  tk.Label(window,text="Expired",font=('Helvetica',10,"bold"),bg="#FD5308").place(x=950,y=0)

		#Bind
		def student_master_Bind_fun(e):

			lookup_records()
			
				

		window.bind("<Return>",student_master_Bind_fun )
		
		window.mainloop()
#________________Student master_________________________

#________________Scan data______________________________


	def Scan_data():
		Scan_Window= tk.Toplevel(User_Window)
		Scan_Window.geometry('1024x550+250+100')
		Scan_Window.resizable(False,False)
		Scan_Window.configure(bg='#ffffff')
		Scan_Window.title("Scan")

		global scan_card_no
		scan_card_no = tk.Entry(Scan_Window)
		scan_card_no.pack()
		scan_card_no.focus_set()

		def scan_card_no_fun(e):
			scan_card_no.focus_set()
			
			scan_card_no.delete(0,"end")
			pass

		Scan_Window.bind("<Return>",scan_card_no_fun )

		Scan_Window.mainloop()


	
#________________Scan data_______________________________

#________________Play / Pause____________________________
	def card_service():
		
		def resume():
			flag = 0
					
			id = int(card_entry.get())
			
			for tuple in row:
				

				if (id == tuple[0] and tuple[0] != "NULL" ):
					new_validity = (datetime.today()).date() + timedelta(days=tuple[3])
					resumequery = "UPDATE student_data set card_validity = '{}' ,cardstatus='Active' where id= {}".format(new_validity,id)
					cursor.execute(resumequery)
					mycon.commit()
					flag = 1
					messagebox.showinfo("Resumed","Card Resumed",parent=card_service_window)

			if flag == 0:

				messagebox.showinfo("Card Number Not Found","Please check Card Number",parent=card_service_window)



		def pause():
			flag = 0

			id = int(card_entry.get())  #cardnumber
			
			for tuple in row:
				
				if (id == tuple[0]):
					pausequery = 'UPDATE student_data set card_validity = NULL ,cardstatus="Pause" where id= {}'.format(id)
					cursor.execute(pausequery)
					mycon.commit()
					flag = 1
					remaing = "Remaing Days ="+str(tuple[3])
					messagebox.showinfo("Paused",remaing,parent=card_service_window)

				
			if flag == 0:

				messagebox.showinfo("Card Number Not Found","Please check Card Number",parent=card_service_window)


		query = cursor.execute('select id,cardstatus,card_validity,days_left from student_data')
		row = cursor.fetchall()

		card_service_window = Toplevel(User_Window)
		card_service_window.title("Pause\Resume Card")
		card_service_window.geometry("400x250+575+315")
		card_service_window.focus()
		card_service_window.resizable(False,False)




				
				
				# Create label frame
		card_service_frame = LabelFrame(card_service_window, text="Card Number")
		card_service_frame.pack(padx=10, pady=10)

				# Add entry box
				
		card_entry = Entry(card_service_frame, font=("Helvetica", 18))
		card_entry.pack(pady=20, padx=20)

				# Add button
		pause_button = Button(card_service_window, text="Pause",width = 21,command=pause)
		pause_button.pack(padx=20, pady=10)

		resume_button = Button(card_service_window, text="Resume",width = 21,command=resume)
		resume_button.pack(padx=20, pady=10)

		devloper_Label =  tk.Label(card_service_window,text="© Developer By ShreeGanesh ☎ :- 9404457569   ",font=('Helvetica',10,"bold")).pack(fill="x",pady=15)

				#Bind
		def card_service_window_Bind_fun(e):
			
			card_entry.focus_set()
			

		card_service_window.bind("<Return>",card_service_window_Bind_fun )
		
		card_service_window.mainloop()




		
			

	

#________________Play / Pause____________________________



#___________User Dash Frontend_________________

	
	#Main.withdraw
	
	User_Window= tk.Toplevel(Main)
	User_Window.geometry('1024x550+250+100')
	User_Window.resizable(False,False)
	User_Window.configure(bg='#ffffff')
	userFrame =tk.LabelFrame(User_Window,font=('Verdana',18,'bold','italic'),
		fg='black',
		borderwidth=10,bg='#F2F2F5',padx=10,pady=5)
	userFrame.pack(fill='x')
	Heading = tk.Label(userFrame ,
		text = "Mess Management System\nUser Dashboard ",
		font= ('Helvetica',19,'bold','italic'),
		bg='#F2F2F5',fg='Black',bd=10).pack(fill='x')
	
	User_label = tk.Label(User_Window,text=("Welcome "+((Username_Entry.get()).capitalize()))
		       ,bg='#ffffff',font=('helvatica',18,'bold'),fg='#67D8DA').pack(pady=20,anchor="center")#place(x=400,y=125)


#__________Right Frame________________________

	RFrame_Buttons = tk.LabelFrame(User_Window,text=' Utilites ',font=('helvatica',14,'bold','italic'),
		fg='black',borderwidth=5,bg='#ffffff',padx=5,pady=5)
	RFrame_Buttons.place(x=865,y=115,)
	#print("Rframe")

#__________Right Frame Buttons_________________
#user.Scan
	Scan_img = ImageTk.PhotoImage(file ='H:/Mess/Assests/user_dash_icons/scan.png')
	Scan_Button = tk.Button(RFrame_Buttons,text='Scan',command=Scan_data,image=Scan_img,borderwidth=0,bg='#ffffff').pack(padx=1)
	Scan_label = tk.Label(RFrame_Buttons,text="Scan",bg='#ffffff',font=('helvatica',10,'bold')).pack()

	def on_closing():
		if messagebox.askokcancel("Logout", "Click on ok to logout.",parent=User_Window):
			User_Window.destroy()


#user . Logout
	logout_img = ImageTk.PhotoImage(file ='H:/Mess/Assests/admin_dash_icons/logout.png')
	logout_Button = tk.Button(RFrame_Buttons,text='Logout',command=on_closing,image=logout_img,borderwidth=0,bg='#ffffff').pack(padx=1)
	logout_label = tk.Label(RFrame_Buttons,text="logout",bg='#ffffff',font=('helvatica',10,'bold')).pack()


#           Left Frame

	Frame_Buttons = tk.LabelFrame(User_Window,text=' Utilites ',font=('helvatica',14,'bold','italic'),
		fg='black',borderwidth=5,bg='#ffffff',padx=5,pady=5)
	Frame_Buttons.place(x=37,y=115,)

	#____________Left Frame Buttons

	Student_master_img = ImageTk.PhotoImage(file ='H:/Mess/Assests/user_dash_icons/student_master.png')
	Student_master_Button = tk.Button(Frame_Buttons,text='Students Master',command=student_master,image=Student_master_img,borderwidth=0,bg='#ffffff').pack(padx=1)
	Student_master_label = tk.Label(Frame_Buttons,text="Students Master",bg='#ffffff',font=('helvatica',10,'bold')).pack()


	card_play_pause_img = ImageTk.PhotoImage(file ='H:/Mess/Assests/user_dash_icons/card_pp.png')
	card_play_pause_Button = tk.Button(Frame_Buttons,text='Pause / Resume',command=card_service,image=card_play_pause_img,borderwidth=0,bg='#ffffff').pack(padx=1)
	card_play_pause_label = tk.Label(Frame_Buttons,text="Pause or Resume\ncard",bg='#ffffff',font=('helvatica',10,'bold')).pack()

	devloper_Label =  tk.Label(User_Window,text="© Developer By ShreeGanesh ☎ :- 9404457569   ",font=('Helvetica',10,"bold")).pack(fill = 'x',anchor = "center",side ="bottom")

	
	


	User_Window.protocol("WM_DELETE_WINDOW", on_closing)
	User_Window.mainloop()

	




	
   
#____________________________________________________________________________________________________________________________

def Login_Screen():
		
	#_______Login Window____________
	global Main
	Main = tk.Tk()
	Main.title('Mess Management System')
	Main.geometry('1024x550+250+100')
	Main.resizable(False,False)

	#_______Background_______________
	Bgimage = ImageTk.PhotoImage(file ='H:/Mess/Assests/bg.png') 
	bgimage = tk.Label(Main,image=Bgimage,borderwidth=0).place(x=0,y=0,)
	#_______Images____________________
	login_img = ImageTk.PhotoImage(file ='H:/Mess/Assests/Login.png')
	reset_img = ImageTk.PhotoImage(file ='H:/Mess/Assests/Reset1.png')

	#_______Labels Login Screen___________________

	frame_1 = tk.LabelFrame(Main,text=' Login Section ',font=('Verdana',18,'bold','italic'),fg='black',borderwidth=10
		,bg='#FEEDD1',padx=50,pady=30)
	frame_1.place(x=250,y=150)

	Username_Label = tk.Label(frame_1,text='Username :-',bd=5,font=('Verdana',17,'bold','italic'),bg='#FEEDD1',fg='Black')
	Username_Label.grid(row=0,column=0,pady=5)

	global Username_Entry 
	Username_Entry = tk.Entry(frame_1,width=15,bd=5,font=('Verdana',14,'bold','italic'),fg='Purple')
	Username_Entry.grid(row=0,column=2,padx=5)

	Password_Label = tk.Label(frame_1,text='Password :-',font=('Verdana',17,'bold','italic'),bg='#FEEDD1',fg='Black')
	Password_Label.grid(row=3,column=0,pady=5)
	
	global Password_Entry
	Password_Entry = tk.Entry(frame_1,width=15,bd=5,show='*',font=('Verdana',14,'bold','italic'),fg='Purple')
	Password_Entry.grid(row=3,column=2,padx=5)

	Login_Button = tk.Button(frame_1,image=login_img,font=('Helvatica',14,'bold','italic'),bg='#FEEDD1',command=Login_Func,borderwidth=0)
	Login_Button.grid(row=4,column=2,pady=20,sticky='e')

	Reset_Button = tk.Button(frame_1,image=reset_img,font=('Helvatica',14,'bold','italic'),bd=0,command=clear,bg='#FEEDD1',)
	Reset_Button.grid(row=4,column=0,pady=20,sticky='w')

	#_______Labels Login Screen___________________


	def dev_info():
		Info = tk.messagebox.showinfo(title="Developers Info", message=' Shri Ganesh Purohit\nContact :9404457569')

	info_img = ImageTk.PhotoImage(file ='H:/Mess/Assests/in.gif')
	info_dev = tk.Button(Main,image = info_img,bg='#FFD42D',command=dev_info,borderwidth=1,bd=0).place(x=480,y=475)



	def clock():
		hour = tm.strftime('%I')
		minute = tm.strftime('%M')
		second = tm.strftime('%S')
		am_pm = tm.strftime('%p')
		date = tm.strftime('%d')
		month = tm.strftime('%b')
		year = tm.strftime('%Y')
		Time_Label.config(text=date+"-"+month+"-"+year+"  "+ hour +":"+ minute +":"+second+':'+am_pm)
		Time_Label.after(1000,clock)
	
	def update():
		Time_Label.config(text='New Time')
		
	Time_Label = tk.Label(frame_1,text=" ",font=('Helvatica',14,'bold','italic'),bg='#FEEDD1',fg='blue',highlightbackground="black")
	Time_Label.grid(row=5,columnspan=3)

	Time_Label.after(5000,update)
	clock()


	#____Set Focus On User Name ______

	Username_Entry.focus_set()

	def on_closing():
		if messagebox.askokcancel("Quit", "Do you want to quit?"):
			Main.destroy()

	Main.protocol("WM_DELETE_WINDOW", on_closing)

	Main.mainloop()

	#________Login Screen___________
Login_Screen()