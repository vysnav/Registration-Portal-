from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #background image

        self.bg=ImageTk.PhotoImage(file="C:/Users/vyshnav/Desktop/DS PROJECT/bg1.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #left vertical background image

        self.bg4=ImageTk.PhotoImage(file="C:/Users/vyshnav/Desktop/DS PROJECT/bg4.png")
        bg4=Label(self.root,image=self.bg4).place(x=80,y=100,width=400,height=500)

        #frame for registration
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTRATION PORTAL",font=("Candara",20,"bold "),bg="white",fg="#3700B3").place(x=50,y=30)
        #---------------------------------------------------------Row 1
        f_name=Label(frame1,text="First Name",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=50,y=100)
        txt_fname=Entry(frame1,font=("candara",15),bg="light grey").place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=370,y=100)
        txt_lname=Entry(frame1,font=("candara",15),bg="light grey").place(x=370,y=130,width=250)

        #---------------------------------------------------------Row 2
        contact=Label(frame1,text="Contact Number",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=50,y=170)
        txt_contact=Entry(frame1,font=("candara",15),bg="light grey").place(x=50,y=200,width=250)

        email=Label(frame1,text="Email Address",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=370,y=170)
        txt_email=Entry(frame1,font=("candara",15),bg="light grey").place(x=370,y=200,width=250)

        #---------------------------------------------------------Row 3
        question=Label(frame1,text="Security Question",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=50,y=240)
        cmbquestion=ttk.Combobox(frame1,font=("candara",13),state="readonly",justify=LEFT)
        cmbquestion['values']=("Select","Your Pet Name","Your Birth Place","Your Best Friend")
        cmbquestion.place(x=50,y=270,width=250)
        cmbquestion.current(0)
        
        answer=Label(frame1,text="Answer",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=370,y=240)
        txt_answer=Entry(frame1,font=("candara",15),bg="light grey").place(x=370,y=270,width=250)

        #---------------------------------------------------------Row 4
        password=Label(frame1,text="Enter Password",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=50,y=310)
        txt_password=Entry(frame1,font=("candara",15),bg="light grey").place(x=50,y=350,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=370,y=310)
        txt_cpassword=Entry(frame1,font=("candara",15),bg="light grey").place(x=370,y=350,width=250)

        #-----terms-----
        chk=Checkbutton(frame1,text="I agree the Terms & Conditions",onvalue=1,offvalue=0,bg="white").place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="C:/Users/vyshnav/Desktop/DS PROJECT/reg_1.png")
        btn=Button(frame1,image=self.btn_img).place(x=50,y=420)
        
root=Tk()
obj=Register(root)
root.mainloop()
