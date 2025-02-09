from tkinter import *
from PIL import Image, ImageTk  # pip installed pillow
from tkinter import ttk, messagebox
import sqlite3

class reportClass:
    def __init__(self, root):
        # Connection 
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+150+200")  # Width, height, x-offset, y-offset
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="View Student Results", font=("goudy old style", 20, "bold"), bg="orange", fg="#262626")
        title.place(x=10, y=15, relwidth=1, height=50)

        # Variables
        self.var_search = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full = StringVar()
        self.var_per = StringVar()
        self.var_id=""

        # Search
        lbl_search = Label(self.root, text="Search By Roll No.", font=("goudy old style", 20, "bold"), bg="white")
        lbl_search.place(x=280, y=100)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20), bg="lightyellow")
        txt_search.place(x=520, y=100, width=150)

        # Buttons
        btn_search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",
                            cursor="hand2", command=self.search)
        btn_search.place(x=680, y=100, width=100, height=35)

        btn_clear = Button(self.root, text='Clear', font=("times new roman", 15), bg="lightgray", activebackground="lightgray",
                           cursor="hand2", command=self.clear)
        btn_clear.place(x=800, y=100, width=100, height=35)

        # Result Labels
        lbl_roll = Label(self.root, text="Roll No", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_roll.place(x=150, y=230, width=150, height=50)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_name.place(x=300, y=230, width=150, height=50)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_course.place(x=450, y=230, width=150, height=50)
        lbl_marks = Label(self.root, text="Marks Obtained", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_marks.place(x=600, y=230, width=150, height=50)
        lbl_full = Label(self.root, text="Full Marks", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_full.place(x=750, y=230, width=150, height=50)
        lbl_per = Label(self.root, text="Percentage", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_per.place(x=900, y=230, width=150, height=50)

        # Dynamic Labels
        self.lbl_roll = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_roll.place(x=150, y=280, width=150, height=50)
        self.lbl_name = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_name.place(x=300, y=280, width=150, height=50)
        self.lbl_course = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_course.place(x=450, y=280, width=150, height=50)
        self.lbl_marks = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_marks.place(x=600, y=280, width=150, height=50)
        self.lbl_full = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_full.place(x=750, y=280, width=150, height=50)
        self.lbl_per = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.lbl_per.place(x=900, y=280, width=150, height=50)

        # Delete Button
        btn_delete = Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="red", cursor="hand2",
                            command=self.delete)
        btn_delete.place(x=500, y=350, width=100, height=35)

    # Search Method
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll=?", (self.var_search.get().strip(),))
                row = cur.fetchone()
                if row:
                    self.var_id=row[0]
                    self.lbl_roll.config(text=row[1])
                    self.lbl_name.config(text=row[2])
                    self.lbl_course.config(text=row[3])
                    self.lbl_marks.config(text=row[4])
                    self.lbl_full.config(text=row[5])
                    self.lbl_per.config(text=row[6])
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    # Clear Method
    def clear(self):
        #self.var_search.set("")
        self.var_id=""
        self.lbl_roll.config(text="")
        self.lbl_name.config(text="")
        self.lbl_course.config(text="")
        self.lbl_marks.config(text="")
        self.lbl_full.config(text="")
        self.lbl_per.config(text="")

    # Delete Method
    #=======Delete function:To delete entry from table=====
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Student Result first ",parent=self.root) 
            else:
                cur.execute("select * from result where rid=? ",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invaild Student Result ",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result deleted Successfully.",parent=self.root)
                        self.clear()
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")


# Main Execution
if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()

# from tkinter import *
# from PIL import Image,ImageTk  # pip installed pillow
# from tkinter import ttk,messagebox
# import sqlite3
# class reportClass:
#     def __init__(self,root):
#         # Connection 
#         self.root=root
#         self.root.title("Student Result Managment System")
#         self.root.geometry("1200x480+150+200")   #width top left
#         self.root.config(bg="white")
#         self.root.focus_force()

#         #=======title=============
#         title=Label(self.root,text="View Student Results",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,relwidth=1,height=50) 
        
#         #===========variables===========
#         self.var_search=StringVar()
#         self.var_roll=StringVar()
#         self.var_name=StringVar()
#         self.var_course=StringVar()
#         self.var_marks=StringVar()
#         self.var_full=StringVar()
#         self.var_per=StringVar()
        
#         ##search ========================
#         lbl_search=Label(self.root,text="Search By Roll No.",font=("goudy old style",20,"bold"),bg="white",compound=self.search).place(x=280,y=100)
#         txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20,),bg="lightyellow").place(x=520,y=100,width=150)
#         #===btn search pannel=======
#         btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command="hand2").place(x=680,y=100,width=100,height=35)
        
#         btn_clear=Button(self.root,text='Clear',font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2").place(x=800,y=100,width=100,height=35)

         
#          #==========Result_labels=======
#         lbl_roll=Label(self.root,text="Roll No",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
#         lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
#         lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
#         lbl_marks=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
#         lbl_full=Label(self.root,text="Full marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
#         lbl_per=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)


#         self_roll=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
#         self_roll.place(x=150,y=280,width=150,height=50)
#         self_name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
#         self_name.place(x=300,y=280,width=150,height=50)
#         self_course=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
#         self_course.place(x=450,y=280,width=150,height=50)
#         self_marks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
#         self_course.place(x=600,y=280,width=150,height=50)
#         self_full=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
#         self_full.place(x=750,y=280,width=150,height=50)
#         self_per=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
#         self_per.place(x=900,y=280,width=150,height=50)

#         #=========button delete========
#         btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="red",cursor="hand2").place(x=500,y=350,width=100,height=35)
        
# #==================================================
#     def search(self):
#             con=sqlite3.connect(database="rms.db")
#             cur=con.cursor()
#             try:
#                 cur.execute(f"select * from result where roll=?",(self.var_search.get(),))
#                 row=cur.fetchone()
#                 if row!=None:
#                     self.roll.config(text="row[1]")
#                     self.name.config(text="row[2]")
#                     self.course.config(text="row[3]")
#                     self.marks.config(text="row[4]")
#                     self.full.config(text="row[5]")
#                     self.per.config(text="row[6]")

#                 else:
#                     messagebox.showerror("Error","No record found",parent=self.root)
#             except Exception as ex:
#                 messagebox.showerror("Error",f"Error due to {str(ex)}")
    

        
# #=====Main root connection to tkinter==========
# if __name__=="__main__":
#         root=Tk()
#         obj=reportClass(root)
#         root.mainloop()