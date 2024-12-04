from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")
 

        img1 = Image.open(r"D:\FaceRecognition\FaceRecognition\background\blog-–-462-1.webp")
        img1 = img1.resize((600, 400), Image.LANCZOS)  # Resize the image to a smaller size
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(relx=0.5, y=100, anchor="n")  # Place the image in the center below the title label

        # Button placed beneath the image
        button = Button(self.root,command=self.face_recog, text="Recognize Face", font=("Times New Roman", 20, "bold"), bg="green", fg="white")
        button.place(relx=0.5, y=520, width=200, height=50, anchor="n")


        title_label = Label(self.root, text="FACE RECOGNITION", font=("Times New Roman", 30, "bold"), bg="white", fg="red")
        title_label.place(relx=0.5, y=0, width=1530, height=80, anchor="n")


    #==============attendance=============================
    def mark_attendance(self,s,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list =[]
            for line in myDataList:
                entry =line.split((","))
                name_list.append(entry[0])

            if((s not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString =now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{r},{n},{d},{d1},Present")



    #==============function=============
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor, minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="Navya",
                    password="cats",
                    database="face_recognition"
                )
                my_cursor = conn.cursor()

                # Fetching details based on predicted id
                my_cursor.execute("select Name from student where Roll=" + str(id))
                n = my_cursor.fetchone()
                print("Name fetch result:", n)  # Debug statement

                my_cursor.execute("select Roll from student where Roll=" + str(id))
                r = my_cursor.fetchone()
                print("Roll fetch result:", r)  # Debug statement

                my_cursor.execute("select Dep from student where Roll=" + str(id))
                d = my_cursor.fetchone()
                print("Dep fetch result:", d)  # Debug statement

                my_cursor.execute("select Student_id from student where Roll=" + str(id))
                s = my_cursor.fetchone()
                print("Student ID fetch result:", s)  # Debug statement

                # Checking if any fetched data is None
                if n is None or r is None or d is None or s is None:
                    print("Data fetch error: One of the values is None")
                    continue

                # Convert fetched values to string
                n = "+".join([str(i) for i in n])
                r = "+".join([str(i) for i in r])
                d = "+".join([str(i) for i in d])
                s = "+".join([str(i) for i in s])

                if confidence > 77:
                    cv2.putText(img, f"Id :{s}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll :{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name :{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep :{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(s, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Another Person", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            
                conn.close()  # Close the connection after each loop
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade =cv2.CascadeClassifier("D:\FaceRecognition\FaceRecognition\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()  
        clf.read("D:\FaceRecognition\FaceRecognition\classifier.xml")

        video_cap = cv2.VideoCapture(0)
        seconds_to_run = 5  # Number of seconds to display the frame
        start_time = cv2.getTickCount()  # Start time for the timer

        while True:
            ret,img = video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to Face recognition",img)

            # Check elapsed time
            elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
            if elapsed_time > seconds_to_run:
                break

            if cv2.waitKey(1)==13:  # Optional: press 'q' to quit earlier
                break


        cv2.destroyAllWindows()
        video_cap.release()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()