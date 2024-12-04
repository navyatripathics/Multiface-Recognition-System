from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import FaceRecognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        Bgimg= Image.open(r"D:\FaceRecognition\FaceRecognition\background\bg_img.jpg")
        Bgimg=Bgimg.resize((1530,710), Image.LANCZOS)
        self.photoBgimg=ImageTk.PhotoImage(Bgimg)

        bg_img=Label(self.root,image=self.photoBgimg)
        bg_img.place(x=0,y=0,width=1530,height=710)

        title_label = Label(self.root, text="Face Recognition Attendance System", 
                            font=("Times New Roman", 30, "bold"), bg="white", fg="black")
        title_label.place(relx=0.5, y=0, width=1530, height=70, anchor="n")

        #button_images
        img1 =Image.open(r"D:\FaceRecognition\FaceRecognition\project_images\image2.jpg")
        img1.thumbnail((240, 260), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1= Button(root,command=self.student_details,cursor="hand2",image = self.photoimg1)
        b1.place(x=100,y=150,width=220,height=220)

        b1_title = Button(root,command=self.student_details, text="Student Details",cursor="hand2" ,font=("Arial", 12, "bold"), bg="ghost white", fg="black")
        b1_title.place(x=100, y=340, width=220, height=40)

        #face detector button
        img2 =Image.open(r"D:\FaceRecognition\FaceRecognition\project_images\face_detect.jpg")
        img2.thumbnail((220, 260), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2= Button(root,command=self.face_data,cursor="hand2",image = self.photoimg2)
        b2.place(x=400,y=150,width=220,height=220)

        b2_title = Button(root,command=self.face_data, text="Face Detector",cursor="hand2" ,font=("Arial", 12, "bold"), bg="white", fg="black")
        b2_title.place(x=400, y=340, width=220, height=40)


        #attendance button
        img3 =Image.open(r"D:\FaceRecognition\FaceRecognition\project_images\image4.jpg")
        img3.thumbnail((220, 260), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3= Button(root,command=self.attendance_data,cursor="hand2",image = self.photoimg3)
        b3.place(x=700,y=150,width=220,height=220)

        b3_title = Button(root,command=self.attendance_data, text="Attendance",cursor="hand2" ,font=("Arial", 12, "bold"), bg="white", fg="black")
        b3_title.place(x=700, y=340, width=220, height=40)

        #help desk
        img4 =Image.open(r"D:\FaceRecognition\FaceRecognition\project_images\image3.jpg")
        img4.thumbnail((220, 260), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4= Button(root,cursor="hand2",image = self.photoimg4)
        b4.place(x=1000,y=150,width=220,height=220)

        b4_title = Button(root, text="Help Desk",cursor="hand2" ,font=("Arial", 12, "bold"), bg="white", fg="black")
        b4_title.place(x=1000, y=340, width=220, height=40)

        #train buttom
        img5 =Image.open(r"D:\FaceRecognition\FaceRecognition\project_images\image6.jpg")
        img5.thumbnail((240, 260), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5= Button(root,command=self.train_data,cursor="hand2",image = self.photoimg5)
        b5.place(x=100,y=400,width=220,height=220)

        b5_title = Button(root,command=self.train_data, text="Train data",cursor="hand2" ,font=("Arial", 12, "bold"), bg="white", fg="black")
        b5_title.place(x=100, y=600, width=220, height=40)

        #photos button
        img6 =Image.open(r"D:\FaceRecognition\FaceRecognition\project_images\image5.jpg")
        img6.thumbnail((220, 260), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6= Button(root,command=self.open_image,cursor="hand2",image = self.photoimg6)
        b6.place(x=400,y=400,width=220,height=220)

        b6_title = Button(root, text="Photos",command=self.open_image,cursor="hand2" ,font=("Arial", 12, "bold"), bg="white", fg="black")
        b6_title.place(x=400, y=600, width=220, height=40)


        #developer button
        img7 =Image.open(r"D:\FaceRecognition\FaceRecognition\project_images\attendance.jpeg")
        img7.thumbnail((220, 260), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b7= Button(root,cursor="hand2",image = self.photoimg7)
        b7.place(x=700,y=400,width=220,height=220)

        b7_title = Button(root, text="Developer",cursor="hand2" ,font=("Arial", 12, "bold"), bg="white", fg="black")
        b7_title.place(x=700, y=600, width=220, height=40)

        #exit
        img8 =Image.open(r"D:\FaceRecognition\FaceRecognition\project_images\exit1.jpg")
        img8.thumbnail((220, 260), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b8= Button(root,cursor="hand2",image = self.photoimg8)
        b8.place(x=1000,y=400,width=220,height=220)

        b8_title = Button(root, text="Exit",cursor="hand2" ,font=("Arial", 12, "bold"), bg="white", fg="black")
        b8_title.place(x=1000, y=600, width=220, height=40)

    def open_image(self):
        os.startfile("data")    

        #===================fucntion buttons===============================================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)   

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)     
 
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    

if __name__ =="__main__":
    root =Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()        