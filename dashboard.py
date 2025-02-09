from tkinter import *
from PIL import Image,ImageTk,ImageDraw  # pip installed pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
from datetime import*
import time
from math import*
import sqlite3

class RMS:
    def __init__(self,root):
        # Connection 
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1550x750+0+0")   #width top left
        self.root.config(bg="white")
         
        #===========Icons===============
        self.logo_dash=ImageTk.PhotoImage(file="education.png")
         
        #===========Title===============
        title=Label(self.root,text="Student Result Managment System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50) 
         
        #============Menu================
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1500,height=80)
         
        #===========Buttons==============
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=250,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=510,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=770,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=1030,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1290,y=5,width=200,height=40)
        
        #=========Content_Window==========
        self.bg_img=Image.open("bg.png") 
        self.bg_img=self.bg_img.resize((920,350),Image.LANCZOS) 
        self.bg_img=ImageTk.PhotoImage(self.bg_img)  #runtime image
         
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=600,y=180,width=900,height=350)
         
         
        #========Update Details==========
        self.lbl_course=Label(self.root,text="Total Course\n[ 0 ]",font=("goudy old style",20),bd=8,relief=RIDGE,bg="#e43b06",fg="white") # bd border
        self.lbl_course.place(x=600,y=530,width=260,height=80)
         
        self.lbl_student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=8,relief=RIDGE,bg="#0676ad",fg="white") # bd border
        self.lbl_student.place(x=900,y=530,width=260,height=80)
         
        self.lbl_result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old style",20),bd=8,relief=RIDGE,bg="#038074",fg="white")# bd border
        self.lbl_result.place(x=1200,y=530,width=260,height=80)
         
        #=====Clock=======
        self.lbl=Label(self.root,text="\nAnalog Clock",font=("Book Antiqua",25,"bold"),compound=BOTTOM,fg="white",bg="#081923",bd=0)
        self.lbl.place(x=100,y=180,height=450,width=350)
        # self.clock_image()
        self.working()
    
        #============Footer=============
        footer=Label(self.root,text="SRMS-Student Result Managment System\nContact Us for any Technical Issue: 987xxxx01",font=("goudy old style",16),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()

    #===========Update Course=============
    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total result\n[{str(len(cr))}]")

            self.lbl_course.after(200,self.update_details)
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")

    #===========Working of clock=================
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        min_=(m/60)*360
        sec=(s/60)*360
        # print(h,m,s)
        # print(hr,min_,sec)
        self.clock_image(hr,min_,sec)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    #===========Image clock function===========
    def clock_image(self,hr,min_,sec):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #=====For Clock Image
        bg=Image.open("images/c.jpg")
        bg=bg.resize((300,300),Image.LANCZOS)
        clock.paste(bg,(50,50))
        # Formula To Rotate the Clock
        # angle_in_radius = angle_in_degrees * math.pi/ 180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = center_x - line_length * math.cos(angle_in_radians)
        # end_y = center_y - line_length * math.sin(angle_in_radians)
        #=====Hour Line Image
        origin=200,200
        draw.line((origin,200+55*sin(radians(hr)),200-55*cos(radians(hr))),fill="#DF005E",width=4)    
        #=====Minute Line Image
        draw.line((origin,200+70*sin(radians(min_)),200-75*cos(radians(min_))),fill="white",width=3)
        #=====Second Line Image
        draw.line((origin,200+90*sin(radians(sec)),200-90*cos(radians(sec))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("images/clock_new.png")

    #=========Calling Functions============
    
    # Add course 
    def add_course(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=CourseClass(self.new_win)
             # Add student 
    def add_student(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=studentClass(self.new_win)
        
        #add result
    def add_result(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=resultClass(self.new_win) 
    
    def add_report(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=reportClass(self.new_win) 
    
    def logout(self):
         op=messagebox.askyesno("confirm","Do you really want to logout?",parent=self.root)
         if op==True:
            self.root.destroy()
            # Redirect to login page
            os.system("python login.py")

    def exit_(self):
         op=messagebox.askyesno("confirm","Do you really want to Exit?",parent=self.root)
         if op==True:
            self.root.destroy()
              
if __name__=="__main__":
        root=Tk()
        obj=RMS(root)
        root.mainloop()
