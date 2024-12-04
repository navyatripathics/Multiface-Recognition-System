import csv
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        img1 = Image.open(r"D:\FaceRecognition\FaceRecognition\project_images\label_left.jpg")
        img1 = img1.resize((650, 200))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        label1 = Label(self.root, image=self.photoimg1)
        label1.place(x=0, y=0, width=650, height=200)  # Place it at the top-left

        img2 = Image.open(r"D:\FaceRecognition\FaceRecognition\project_images\atten_bg.jpeg")
        img2 = img2.resize((700, 200))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        label2 = Label(self.root, image=self.photoimg2)
        label2.place(x=650, y=0, width=700, height=200)

        title_label = Label(self.root, text="ATTENDANCE DETAILS", 
                            font=("Times New Roman", 30, "bold"), bg="blue", fg="white")
        title_label.place(x=0, y=200, width=1530, height=40)

        main_frame = Frame(self.root, bd=2, bg="black")
        main_frame.place(x=0, y=240, width=1494, height=600)

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=5, width=610, height=580)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE)
        left_inside_frame.place(x=0, y=5, width=605, height=270)

        # Labels and entry fields
        self.attendance_id_entry = self.create_entry(left_inside_frame, "Attendance Id", 0, 0)
        self.student_roll_entry = self.create_entry(left_inside_frame, "Roll No.", 1, 0)
        self.student_name_entry = self.create_entry(left_inside_frame, "Student Name", 2, 0)
        self.depEntry = self.create_entry(left_inside_frame, "Department", 3, 0)
        self.attnTime = self.create_entry(left_inside_frame, "Time", 4, 0)
        self.attnDate = self.create_entry(left_inside_frame, "Date", 5, 0)

        # Attendance Status Combobox
        attenLabel = Label(left_inside_frame, text='Attendance ', font=("times new roman", 12, "bold"))
        attenLabel.grid(row=6, column=0, padx=5, pady=5, sticky=W)
        self.atten_combo = ttk.Combobox(left_inside_frame, font=("times new roman", 12), state="readonly", width=17)
        self.atten_combo["values"] = ("Status", "Present", "Absent")
        self.atten_combo.current(0)
        self.atten_combo.grid(row=6, column=1, padx=2, pady=10)

        # Button Frame with commands
        bt_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="beige")
        bt_frame.place(x=0, y=300, width=600, height=39)

        Button(bt_frame, text="Import CSV", width=16, font=("times new roman", 12, "bold"),
               command=self.import_csv, bg="beige", fg="dark green").grid(row=0, column=0, sticky=W)
        Button(bt_frame, text="Export CSV", width=16, font=("times new roman", 12, "bold"),
               command=self.export_csv, bg="beige", fg="dark green").grid(row=0, column=1, sticky=W)
        Button(bt_frame, text="RESET", width=15, font=("times new roman", 12, "bold"),
               command=self.reset_fields, bg="beige", fg="dark green").grid(row=0, column=2, sticky=W)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=640, y=5, width=610, height=580)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=595, height=358)

        # Scrollbars and Table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("Id", "Roll No.", "Name", "Department", 
                                                                        "Time", "Date", "Attendance"), 
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # Table Headers
        for col in self.AttendanceReportTable["columns"]:
            self.AttendanceReportTable.heading(col, text=col)
            self.AttendanceReportTable.column(col, width=100)

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

    def create_entry(self, frame, label_text, row, col):
        label = Label(frame, text=label_text, font=("times new roman", 12, "bold"))
        label.grid(row=row, column=col, padx=5, pady=5, sticky=W)
        entry = ttk.Entry(frame, width=18, font=("times new roman", 13))
        entry.grid(row=row, column=col+1, padx=5, pady=5, sticky=W)
        return entry

    def reset_fields(self):
        self.attendance_id_entry.delete(0, END)
        self.student_roll_entry.delete(0, END)
        self.student_name_entry.delete(0, END)
        self.depEntry.delete(0, END)
        self.attnTime.delete(0, END)
        self.attnDate.delete(0, END)
        self.atten_combo.current(0)

    def import_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        with open(file_path, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                self.AttendanceReportTable.insert("", END, values=row)

    def export_csv(self):
        if not self.AttendanceReportTable.get_children():
            messagebox.showerror("Error", "No data to export.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Id", "Roll No.", "Name", "Department", "Time", "Date", "Attendance"])
                for row_id in self.AttendanceReportTable.get_children():
                    writer.writerow(self.AttendanceReportTable.item(row_id)["values"])
            messagebox.showinfo("Export", "Data exported successfully!")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
