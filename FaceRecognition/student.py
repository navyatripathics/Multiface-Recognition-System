from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        #=====variables======
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()

        # Load and set background image
        bg_image = Image.open(r"D:\FaceRecognition\FaceRecognition\background\background.png")
        bg_image = bg_image.resize((1530, 800), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Create a label to hold the background image
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Title label
        title_label = Label(self.root, text="STUDENT DETAILS", 
                            font=("Times New Roman", 30, "bold"), bg="blue", fg="white")
        title_label.place(relx=0.5, y=0, width=1530, height=70, anchor="n")

        # Main frame for left and right sections
        main_frame = Frame(self.root, bd=2, bg="black")
        main_frame.place(x=0, y=55, width=1494, height=600)

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=15, y=10, width=650, height=580)

        # Add image to the left frame
        img_left=Image.open(r"D:\FaceRecognition\FaceRecognition\project_images\label_left.jpg")
        img_left=img_left.resize((520,110))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_label=Label(Left_frame,image=self.photoimg_left)
        f_label.place(x=10,y=10,width=610,height=110)


        # Label to hold the student image
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=630, height=130)

        # Current Course section (placed after the image)
        current_course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=10, y=140, width=630, height=150)

        #course
        course_label = Label(current_course_frame,text ='Course',font=("times new roman", 12, "bold"))
        course_label.grid(row=0,column=0)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 12, "bold"),state="readonly",width=17)
        course_combo["values"]= ("Select Course","B.Tech.","MBA","BBA","BCA","B.pharm","MCA" )
        course_combo.current(0)
        course_combo.grid(row=0,column=1)

         #year
        year_label = Label(current_course_frame, text='Year', font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 12),state="readonly", width=17)
        year_combo["values"] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1,padx=2,pady=10)

        #department
        dep_label = Label(current_course_frame,text ='Department',font=("times new roman", 12, "bold"))
        dep_label.grid(row=2,column=0,padx=10)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 12),state="readonly",width=17)
        dep_combo["values"]= ("Select Department","CSE","CS- AIML","CS-AI","AIML","AI","IOT","CYS","DS","Other" )
        dep_combo.current(0)
        dep_combo.grid(row=2,column=1,padx=2,pady=10)

        # Class student information (placed after the image)
        class_student_information = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class Student Information",
                                               font=("times new roman", 12, "bold"))
        class_student_information.place(x=10, y=290, width=630, height=260)

        # University Roll No.
        student_roll = Label(class_student_information, text='Roll No.', font=("times new roman", 12, "bold"))
        student_roll.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        student_roll_entry = ttk.Entry(class_student_information,textvariable=self.var_roll, width=20, font=("times new roman", 13))
        student_roll_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Student Name
        student_name = Label(class_student_information, text='Student Name', font=("times new roman", 12, "bold"))
        student_name.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        student_name_entry = ttk.Entry(class_student_information,textvariable=self.var_std_name, width=18, font=("times new roman", 13))  # Adjusted width
        student_name_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Date of Birth
        student_dob = Label(class_student_information, text='DOB', font=("times new roman", 12, "bold"))
        student_dob.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        student_dob_entry = ttk.Entry(class_student_information,textvariable=self.var_dob, width=20, font=("times new roman", 13))
        student_dob_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Phone No.
        student_phone = Label(class_student_information, text='Phone No.', font=("times new roman", 12, "bold"))
        student_phone.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        student_phone_entry = ttk.Entry(class_student_information,textvariable=self.var_phone, width=18, font=("times new roman", 13))
        student_phone_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Email
        student_email = Label(class_student_information, text='Email', font=("times new roman", 12, "bold"))
        student_email.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        student_email_entry = ttk.Entry(class_student_information,textvariable=self.var_email, width=20, font=("times new roman", 13))
        student_email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Studnet Id.
        student_id = Label(class_student_information, text='Student Id', font=("times new roman", 12, "bold"))
        student_id.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        student_id_entry = ttk.Entry(class_student_information,textvariable=self.var_std_id, width=18, font=("times new roman", 13))
        student_id_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        #radio buttons
        self.var_radio1= StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_information,variable=self.var_radio1,text = "Take photo Sample",value ="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2 = ttk.Radiobutton(class_student_information,text = "No photo Sample",variable=self.var_radio1,value ="No")
        radiobtn2.grid(row=6,column=1)



        #buttons frame
        bt_frame=Frame(class_student_information,bd=2,relief=RIDGE,bg="beige")
        bt_frame.place(x=0,y=160,width=600,height=39)


        save_btn=Button(bt_frame,text="SAVE",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="beige",fg="dark green")
        save_btn.grid(row=0,column=0,sticky=W)

        update_btn=Button(bt_frame,text="UPDATE",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="beige",fg="dark green")
        update_btn.grid(row=0,column=1,sticky=W)

        del_btn=Button(bt_frame,text="DELETE",command=self.delete_data,width=16,font=("times new roman",12,"bold"),bg="beige",fg="dark green")
        del_btn.grid(row=0,column=2,sticky=W)

        reset_btn=Button(bt_frame,text="RESET",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="beige",fg="dark green")
        reset_btn.grid(row=0,column=3,sticky=W)

        bt2_frame=Frame(class_student_information,bd=2,relief=RIDGE,bg="beige")
        bt2_frame.place(x=0,y=200,width=600,height=39)

        takephoto_btn=Button(bt2_frame,text="Take photo sample",command=self.generate_dataset,width=33,font=("times new roman",12,"bold"),bg="brown",fg="white")
        takephoto_btn.grid(row=0,column=0,sticky=W)

        updatephoto_btn=Button(bt2_frame,text="Update photo sample",width=33,font=("times new roman",12,"bold"),bg="brown",fg="beige")
        updatephoto_btn.grid(row=0,column=1,sticky=W)
        

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=675, y=10, width=660, height=580)

        Search_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman", 12, "bold"))
        Search_frame.place(x=0,y=10,width=710,height=100)

        search_label =Label(Search_frame,text="Search By:", font=("times new roman", 15, "bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo = ttk.Combobox(Search_frame,font=("times new roman", 12),state="readonly",width=17)
        search_combo["values"]= ("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(Search_frame, width=18, font=("times new roman", 13))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        
        search_btn = Button(Search_frame,text="Search",width=17, bg="red",fg="white",font=("times new roman", 12, "bold"))
        search_btn.grid(row=1,column=2,padx=5)

        show_all_btn = Button(Search_frame,text="Show All",width=14, bg="black",fg="white",font=("times new roman", 12, "bold"))
        show_all_btn.grid(row=1,column=1)

        # table_frame
        table_frame = Frame(Right_frame,bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=5,y=150,width=595,height=250)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("Dep","Course","Year","Id","Name","Roll no","DOB","Email","Phone","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)

        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Id", text="Student ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Roll no", text="Roll Number")
        self.student_table.heading("DOB", text="Date of Birth")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone Number")
        self.student_table.heading("Photo", text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("Dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Id", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Roll no", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Photo", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #==============function declaration=================
    def add_data(self):
        if self.var_dep.get() =="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_roll.get()=="" or self.var_phone.get()=="" or self.var_email.get() =="" or self.var_dob.get()=="":
            messagebox.showerror("Error","Enter all fields",parent= self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username = "Navya",
                    password="cats",
                    database="face_recognition"
                )  
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_roll.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_radio1.get()))


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Details has been added Successfully",parent =self.root)
            except Exception as es:
                messagebox.showerror("error",f"Due to: {str(es)}",parent= self.root)    

    def fetch_data(self):
        conn = mysql.connector.connect(
                    host="localhost",
                    username = "Navya",
                    password="cats",
                    database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()        
        

    #get_cursor function
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_std_id.set(data[3])
        self.var_std_name.set(data[4])
        self.var_roll.set(data[5])
        self.var_dob.set(data[6])
        self.var_email.set(data[7])
        self.var_phone.set(data[8])
        self.var_radio1.set(data[9])


    #update function
    def update_data(self):
        if self.var_dep.get() =="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_roll.get()=="" or self.var_phone.get()=="" or self.var_email.get() =="" or self.var_dob.get()=="":
            messagebox.showerror("Error","Enter all fields",parent= self.root)
        else:
            try:
                update_ask = messagebox.askyesno("Update","Do you want to update this details?",parent =self.root)
                if update_ask >0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username = "Navya",
                        password="cats",
                        database="face_recognition")  
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep =%s,Course =%s,Year =%s,Student_id =%s,Name = %s,Roll = %s,Dob=%s,Email =%s,Phone =%s,PhotoSample=%s where Roll=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_roll.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_radio1.get(),self.var_roll.get()))
                else:
                    if not update_ask:
                        return   

                messagebox.showinfo("Success","Update Completed",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{(es)}",parent = self.root)

    #delete function
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student roll no. is must",parent=self.root)
        else:
            try:
                delete= messagebox.askyesno("Delete Record","Do you want to delete the student",parent =self.root)
                if delete:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username = "Navya",
                        password="cats",
                        database="face_recognition")  
                    my_cursor = conn.cursor()
                    sql = "delete from student where Roll=%s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student record")    
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{(es)}",parent = self.root)

    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_dob.set("")            
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")

    #========photo generated dataset=================
    def generate_dataset(self):
        if self.var_dep.get() =="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_roll.get()=="" or self.var_phone.get()=="" or self.var_email.get() =="" or self.var_dob.get()=="":
            messagebox.showerror("Error","Enter all fields",parent= self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username = "Navya",
                    password="cats",
                    database="face_recognition")  
                my_cursor = conn.cursor()
             

                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
  
                my_cursor.execute("update student set Dep =%s,Course =%s,Year =%s,Student_id =%s,Name = %s,Dob=%s,Email =%s,Phone =%s,PhotoSample=%s where Roll=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_radio1.get(),self.var_roll.get()))

                self.fetch_data()
                self.reset_data()
                conn.close()    

                face_classifier = cv2.CascadeClassifier("D:\FaceRecognition\FaceRecognition\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5) #scaling factor , minimum neighbour
                    
                    for (x,y,w,h) in  faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap =cv2.VideoCapture(0)
                img_id =0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))    
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed")    
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                print(str(es))
                    

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
