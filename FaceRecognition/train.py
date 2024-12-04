from tkinter import *
from tkinter import messagebox
from PIL import Image
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        title_label = Label(self.root, text="Train Dataset", 
                            font=("Times New Roman", 30, "bold"), bg="white", fg="green")
        title_label.place(relx=0.5, y=0, width=1530, height=80, anchor="n")

        b1_title = Button(self.root, command=self.train_classifier, text="Train Data", cursor="hand2",
                          font=("Arial", 12, "bold"), bg="blue", fg="white")
        b1_title.place(x=0, y=340, width=1350, height=40)

    def train_classifier(self):
        data_dir = "data" 
        if not os.path.isdir(data_dir):
            messagebox.showerror("Error", "Data directory does not exist.")
            return

        # List all images in the data directory
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.jpg') or file.endswith('.png')]
        if not path:
            messagebox.showerror("Error", "No images found in the data directory.")
            return

        faces = []
        ids = []

        for image_path in path:
            img = Image.open(image_path).convert('L')  # Convert image to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image_path)[1].split('.')[1])
            print(f"Processing image: {image_path} with ID: {id}")  # Debugging line

            faces.append(imageNp)
            ids.append(id)
            # Display image during training (optional, can be removed for faster processing)
            cv2.imshow("Training on image...", imageNp)
            cv2.waitKey(1)  # Display each image briefly

        ids = np.array(ids, dtype=np.int32)    

        # Train the classifier
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write(r"D:\FaceRecognition\FaceRecognition\classifier.xml")  # Save the trained model
            messagebox.showinfo("Result", "Training datasets completed successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Training failed: {str(e)}")

        cv2.destroyAllWindows()  # Close all OpenCV windows

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
