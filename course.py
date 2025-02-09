from tkinter import *
from PIL import Image,ImageTk  # pip installed pillow
from tkinter import ttk,messagebox
import sqlite3
class CourseClass:
    def __init__(self,root):
        # Connection 
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1200x480+150+200")   #width top left
        self.root.config(bg="white")
        self.root.focus_force()

        #=======title=============
        title=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,relwidth=1,height=35) 

        #========Variables========
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

        #========Widgets===========
        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

        #========Entry Fields======
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_courseName.place(x=150,y=60,width=200)
        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_description.place(x=150,y=180,width=500,height=130)

        #=======Buttons============
        self.btn_add=Button(self.root,text='Save',font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text='Update',font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.Update)
        self.btn_add.place(x=270,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_add.place(x=390,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_add.place(x=510,y=400,width=110,height=40)

        #=======Search Panel========
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)

        #=================Content=====================
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)
        # Set scroll bar
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollX=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollX.set,yscrollcommand=scrolly.set)
        # Pack scroll bar
        scrollX.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        # Config scroll bar in x and y view 
        scrollX.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        # Heading of the Table
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings' 
        # Given column wise width
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1)
        #=========Bind is a function that select data from table and show it in text fields========
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data) 
        self.show() # Show the data on input field
#======================================================
#=======Clear function:Set all functions to clear======
    def clear(self):
        self.show() # Show the data on input field
        self.var_course.set("") #For course
        self.var_duration.set("") #For duration
        self.var_charges.set("") #For charges
        self.var_search.set("") # For search 
        self.txt_description.delete('1.0',END) 
        self.txt_courseName.config(state=NORMAL)

#=======Delete function:To delete entry from table=====
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required. ",parent=self.root)
            else:
                cur.execute("select * from course where name=? ",(self.var_course.get(),))
                row=cur.fetchone()
                #  print(row)
                if row==None:
                    messagebox.showerror("Error","Please select course from the list. ",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted Successfully.",parent=self.root)
                        self.clear()
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")

#==============Get data from table to text fields======
    def get_data(self,ev):
        # config txt_courseName as we can't change course but can read only
        self.txt_courseName.config(state='readonly')
        r=self.CourseTable.focus() # used to focus data
        content=self.CourseTable.item(r) #get data one by one
        row=content["values"] #get values of each data
        # print(row)   
        # the below function set the data by its index
        self.var_course.set(row[1]) #For course
        self.var_duration.set(row[2]) #For duration
        self.var_charges.set(row[3]) #For charges
        self.txt_description.delete('1.0',END) 
        self.txt_description.insert(END,row[4])#For description

#===============Create database connection=============
#===============Add the data to the table==============
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                  messagebox.showerror("Error","Course Name should be required. ",parent=self.root)
            else:
                cur.execute("select * from course where name=? ",(self.var_course.get(),))
                row=cur.fetchone()
                #  print(row)
                if row!=None:
                    messagebox.showerror("Error","Course Name already present. ",parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,charges,description) values(?,?,?,?)",(self.var_course.get(),
                     self.var_duration.get(),
                     self.var_charges.get(),
                     self.txt_description.get("1.0",END)))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.show() # Show the data on input field
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")

#============To Update the data from the table=========
    def Update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                  messagebox.showerror("Error","Course Name should be required. ",parent=self.root)
            else:
                cur.execute("select * from course where name=? ",(self.var_course.get(),))
                row=cur.fetchone()
                #  print(row)
                # Course can't be updated first you have to delete it and then add it
                if row==None:
                    messagebox.showerror("Error","Select Course from list. ",parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where name=?",(
                     self.var_duration.get(),
                     self.var_charges.get(),
                     self.txt_description.get("1.0",END),self.var_course.get()
                     ))
                    con.commit()
                    messagebox.showinfo("Success","Course Update Successfully",parent=self.root)
                    self.show() # Show the data on input field
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    #=====Used to show the input data to table=========
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                 self.CourseTable.insert('',END,values=row) 
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                 self.CourseTable.insert('',END,values=row) 
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")
    
#=====Main root connection to tkinter==========
if __name__=="__main__":
        root=Tk()
        obj=CourseClass(root)
        root.mainloop()