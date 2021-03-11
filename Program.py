from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #background image

        self.bg=ImageTk.PhotoImage(file="images/bg1.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,width=1920,height=1080)

        #left vertical background image

        self.bg4=ImageTk.PhotoImage(file="images/bg4.png")
        bg4=Label(self.root,image=self.bg4).place(x=80,y=100,width=400,height=500)

        #frame for registration
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTRATION PORTAL",font=("Candara",20,"bold "),bg="white",fg="#3700B3").place(x=50,y=30)
        #---------------------------------------------------------Row 1
    
        f_name=Label(frame1,text="First Name",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("candara",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)


        l_name=Label(frame1,text="Last Name",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("candara",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        #---------------------------------------------------------Row 2
        contact=Label(frame1,text="Contact Number",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("candara",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email Address",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("candara",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        #---------------------------------------------------------Row 3
        question=Label(frame1,text="Security Question",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=50,y=240)

        self.cmbquestion=ttk.Combobox(frame1,font=("candara",13),state="readonly",justify=LEFT)
        self.cmbquestion['values']=("Select","Your pet name","Your birth place","Your best friend")
        self.cmbquestion.place(x=50,y=270,width=250)
        self.cmbquestion.current(0)
        
        answer=Label(frame1,text="Answer",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("candara",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        #---------------------------------------------------------Row 4
        password=Label(frame1,text="Enter Password",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("candara",15),bg="light grey")
        self.txt_password.place(x=50,y=350,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("Candara",15,"bold "),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("candara",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=350,width=250)

        #-----terms-----
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I agree the Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white").place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="images/reg_1.png")
        self.sign_img=ImageTk.PhotoImage(file="images/sign_in.jpg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=90,y=420)
        btn_login=Button(frame1,image=self.sign_img,bd=0,cursor="hand2").place(x=410,y=420)

    def register_data(self):
        if(self.txt_fname.get()=="" or self.txt_lname.get()=="" or  self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmbquestion.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" ):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif(self.txt_password.get()!=self.txt_cpassword.get()):
            messagebox.showerror("Error","Passwords doesn't match",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Terms & Condition not verified!",parent=self.root)
        else:
            messagebox.showinfo("Success","Rgistration successful",parent=self.root)
            


             
        
root=Tk()
obj=Register(root)
root.mainloop()
