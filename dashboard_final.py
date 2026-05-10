import tkinter as tk
import ttkbootstrap as ttk 
from ttkbootstrap.constants import *
from tkinter import messagebox
from datetime import datetime

WEEKLY_SCHEDULE = { 
    "Monday": [("CCO3", "Boss. John Christian Lor ", "07:00 AM - 12:00 AM"), ("NSTP", "Ma'am Cheong ", "05:00 PM - 08:00 PM")],
    "Tuesday": [("No Classes", "-", "-")],
    "Wednesday": [("ETHICS", "Atty. Jullius Cabasag", "10:30 PM - 01:30 PM"),("UTS", "Ma'am. Pretty Stephanie", "05:30 PM - 08:30 PM")],
    "Thursday": [("TCW", "Prof. Mark Anthony ", "05:00 PM - 08:30 PM")],
    "Friday": [("Living in IT ERA", "Ma'am Elizah Alquizar ", "07:00 AM - 10:00 AM")],
    "Saturday": [("STS", "Maam Jeanette Tusi", "07:00 AM - 10:00 PM"),("FILDIS", "Sir. Danilo", "10:30 AM - 12:00 PM"),("PATHFIT", "Sir. Clip Harrold ", "04:00 PM - 07:00 PM")],
    "Sunday": [("No Classes", "-", "-")]
}

window = ttk.Window(themename="superhero")
window.geometry("1366x768") 
window.title("Batch 2 Project")

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)

for frame in (frame1, frame2, frame3, frame4):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

def show_frame(frame):
    frame.tkraise() 

def create_sidebar(parent_frame):
    sidebar = ttk.Frame(parent_frame, borderwidth=2, relief="solid")
    sidebar.place(x=0, y=0, relwidth=0.2, relheight=1)
    
    btn_dashboard = ttk.Button(sidebar, text="Dashboard", bootstyle="outline-info", command=lambda: show_frame(frame2))
    btn_dashboard.place(relx=0.1, rely=0.1, relwidth=0.8, height=50)

    btn_schedule = ttk.Button(sidebar, text="Schedule", bootstyle="outline-info", command=lambda: show_frame(frame3))
    btn_schedule.place(relx=0.1, rely=0.2, relwidth=0.8, height=50)

    btn_grades = ttk.Button(sidebar, text="Grades", bootstyle="outline-info", command=lambda: show_frame(frame4))
    btn_grades.place(relx=0.1, rely=0.3, relwidth=0.8, height=50)

    btn_logout = ttk.Button(sidebar, text="Logout", bootstyle="outline-danger", command=lambda: show_frame(frame1))
    btn_logout.place(relx=0.1, rely=0.9, relwidth=0.8, height=50)

def login():
    user_name = "Student12" 
    pass_word = "12345"
    if login_entry_username.get() == user_name and login_entry_password.get() == pass_word:
        messagebox.showinfo(title="Logged In Success", message="You Successfully Logged In")
        show_frame(frame2) 
    else:
        messagebox.showerror(title="Error", message="Log In Failed")

######################## LOGIN PAGE (Frame 1)

login_label = ttk.Label(frame1, text="LOG IN", font=("Arial", 20), bootstyle="danger")
login_label.pack(pady=(200, 20))


admin_label = ttk.Label(frame1, text="Student ID / Admin", font=("Arial", 10), bootstyle="light")
admin_label.place(x=560, y=255)

login_entry_username = ttk.Entry(frame1, width=40, bootstyle="light solid", foreground="white")
login_entry_username.place(x=560, y=280)

admin_label2 = ttk.Label(frame1, text="Password", font=("Arial", 10), bootstyle="light")
admin_label2.place(x=560, y=310)

login_entry_password = ttk.Entry(frame1, show="*", width=40, bootstyle="light")
login_entry_password.place(x=560, y=335)

login_button1 = ttk.Button(frame1, width=10, text="ADMIN", bootstyle="success, outline", command=login)
login_button1.place(x=580, y=380)

login_button2 = ttk.Button(frame1, width=10, text="STUDENT", bootstyle="success, outline", command=login)
login_button2.place(x=690, y=380)


######################## DASHBOARD PAGE (Frame 2)
try:
    image1 = tk.PhotoImage(file="dashboard.png")
    dashboard_image = tk.PhotoImage(file="boy.png")
    bg_dashboard = tk.PhotoImage(file="image.png")
    medal_image = tk.PhotoImage(file="rewards.png")
except:
    image1 = dashboard_image = bg_dashboard = medal_image = None

#--------------student dashboard / student message / scholl name
student_dashboard_label = ttk.Label(frame2, image=image1, compound=LEFT, text=" STUDENT DASHBOARD", width=500, padding=5) 
student_dashboard_label.configure(font=("arial", 30), bootstyle="inverse secondary")
student_dashboard_label.pack(fill=X)
student_message_label = ttk.Label(frame2, text="Welcome, Student! We’re glad to have you here!", font=("roboto", 15, "bold"), bootstyle="success", wraplength=800, justify="center")
student_message_label.place(x=500, y=140)
school_name_label = ttk.Label(frame2, text="PAMANTASAN NG LUNGSOD NG VALENZUELA", font=("roboto", 25, "bold"), bootstyle="info", wraplength=800)
school_name_label.place(x=400, y=80)
logout_button = ttk.Button(frame2, text="Log Out", bootstyle="outline-danger")
logout_button.place(x=1200, y=18, width=150)
admin_view_button = ttk.Button(frame2, text="Admin View", bootstyle="outline-success")
admin_view_button.place(x=1040, y=18, width=150)
#--------------------------lines-------------------------------------------
line4 = ttk.Separator(frame2, orient=HORIZONTAL, bootstyle="light")
line4.place(y=81, x=260, width=1095)
line5 = ttk.Separator(frame2, orient=HORIZONTAL, bootstyle="light")
line5.place(y=120, x=260, width=1095)
line6 = ttk.Separator(frame2, orient=VERTICAL, bootstyle="light")
line6.place(width=2, height=270, y=80, x=1354)
#--------------------------content--------------------------------------------------
content_frame1 = ttk.Frame(frame2, border=2, borderwidth=5, relief="solid")
content_frame1.place(x=300, y=200, height=200, width=800) 
#---------------------------center profile----------------------------------------
center_profile_label = ttk.Label(frame2, text="PROFILE", font=("Arial", 20, "bold"), bootstyle="danger")
center_profile_label.place(x=620, y=190)
#-------------------------------seperator--------------------------------
line3 = ttk.Separator(frame2, orient=HORIZONTAL, bootstyle="light")
line3.place(x=330, y=230, width=750)
line3_1 = ttk.Separator(frame2, orient=HORIZONTAL, bootstyle="light")
line3_1.place(x=330, y=380, width=750)
#--------------------------content-------------------------------------
content_frame2 = ttk.Frame(frame2, border=2, borderwidth=5, relief="solid")
content_frame2.place(x=300, y=430, height=250, width=800) 
#-----------------student info / student name / student year / student course
student_info_label = tk.Label(frame2, image=dashboard_image)
student_info_label.place(x=350, y=240)
student_name_label = ttk.Label(frame2, text="Unknown User", font=("arial", 20, "bold"), bootstyle="light")
student_name_label.place(x=500, y=260)
student_name_year = ttk.Label(frame2, text="SCHOOL YEAR : 2025 - 2026", font=("arial", 15, "bold"), bootstyle="light")
student_name_year.place(x=501, y=300)
student_name_course = ttk.Label(frame2, text="BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY", font=("arial", 15, "bold"), bootstyle="light")
student_name_course.place(x=501, y=330)
#-----------------------------left border------------------------------------
left_border_frame = ttk.Frame(frame2, border=2, relief="solid", borderwidth=5)
left_border_frame.place(x=10, y=80, height=135, width=250)
left_border_frame2 = ttk.Frame(frame2, border=2, relief="solid", borderwidth=5)
left_border_frame2.place(x=10, y=225, height=220, width=250)
left_border_frame3 = ttk.Frame(frame2, border=2, relief="solid", borderwidth=5)
left_border_frame3.place(x=10, y=460, height=220, width=250)
system_label = ttk.Label(frame2, text="STUDENT SYSTEM", font=("arial", 15 , "bold"), bootstyle="danger")
system_label.place(x=40, y=235)
schedule_button = ttk.Button(frame2, text="SCHEDULE", bootstyle="outline-info", command=lambda: show_frame(frame3))
schedule_button.place(x=35, y=280, width=200, height=60)
grade_button = ttk.Button(frame2, text="GRADE", bootstyle="outline-success", command=lambda: show_frame(frame4))
grade_button.place(x=35, y=360, width=200, height=60)
schedule_line = ttk.Separator(frame2, orient=HORIZONTAL, bootstyle="light")
schedule_line.place(x=30, y=268, width=212)
rank_label = ttk.Label(frame2, text="RANK", font=("arial", 15, "bold"), bootstyle="danger")
rank_label.place(x=105, y=450)
medal_label = ttk.Label(frame2,image=medal_image, text="TOP?", font=('arial',30, "bold"),compound=TOP, bootstyle="warning")
medal_label.place(x=68, y=490)
#------------------------bg container--------------------------------------
bg_container = tk.Label(frame2, image=bg_dashboard)
bg_container.place(x=13, y=82, width=244, height=130)
#------------------------right border and label------------------------
right_border = ttk.Frame(frame2, border=2, relief="solid", borderwidth=5)
right_border.place(x=1120, y=350, height=330, width=235)
right_border2 = ttk.Frame(frame2, border=2, relief="solid", borderwidth=5)
right_border2.place(x=1130, y=360, height=310, width=215)
right_label = ttk.Label(frame2, text="LEADERBOARD", font=("arial", 15, "bold"), bootstyle="danger")
right_label.place(x=1162, y=340)
ave_label = ttk.Label(frame2, text="AVE: ____________", font=("arial", 15, "bold"), bootstyle="success")
ave_label.place(x=1140, y=620)
medal_line = ttk.Separator(frame2, orient=HORIZONTAL, bootstyle="light")
medal_line.place(x=1130, y=600, width=212)
#------------------------seperator---------------------------------------
line = ttk.Separator(frame2, orient=HORIZONTAL, bootstyle="light")
line.place(y=415, x=260, width=860)
#-----------------------schedule---------------------------------------
schedule_label = ttk.Label(frame2, text="SCHEDULE TODAY", font=("Arial", 20, "bold"), bootstyle="danger")
schedule_label.place(x=550, y=420)
#----------------------seperator-------------------------------------
line2 = ttk.Separator(frame2, orient=HORIZONTAL, bootstyle="light")
line2.place(x=300, y=460, width=800)
#--------------------date entry / date label-----------------------------
date_label = ttk.Label(frame2, text="DATE", font=("Segoe UI", 15, "bold"))
date_label.place(x=1120, y=210)
date_entry = ttk.DateEntry(frame2, bootstyle="danger")
date_entry.place(x=1120, y=240, width=200)
#-------------------------date title---------------------------------------
date_title = ttk.Label(frame2, text="Current Time", font=("Segoe UI", 16, "bold"))
date_title.place(x=1120, y=273)
#-------------------------time label---------------------------------------------
time_label = ttk.Label(frame2, font=("Segoe UI", 15, "bold"), bootstyle="info")
time_label.place(x=1120, y=304)

def update_time():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    frame2.after(1000, update_time)

update_time()
#--------------------------SCHEDULE TODAY--------------------------------
columns = ("subject", "professor", "time")
sched_table = ttk.Treeview(content_frame2, columns=columns, show="headings", height=7)
sched_table.heading("subject", text="SUBJECT CODE")
sched_table.heading("professor", text="PROFESSOR")
sched_table.heading("time", text="SCHEDULED TIME")
sched_table.column("subject", width=150, anchor=CENTER)
sched_table.column("professor", width=250, anchor=CENTER)
sched_table.column("time", width=350, anchor=CENTER)
sched_table.place(x=19, y=50, height=170)

def update_dashboard_data():
    #--------------------- Update Time
    now = datetime.now()
    time_label.config(text=now.strftime("%I:%M:%S %p"))
    
    # -------------Update Subject Table based on Day
    current_day = now.strftime("%A")
    # --------------------Clear table first
    for item in sched_table.get_children():
        sched_table.delete(item)
    
    # -------------------Insert today's classes
    today_classes = WEEKLY_SCHEDULE.get(current_day, [])
    for subject, prof, time in today_classes:
        sched_table.insert("", END, values=(subject, prof, time))
    
    frame2.after(1000, update_dashboard_data)

######################## SCHEDULE PAGE (Frame 3)
create_sidebar(frame3)

content_f3 = ttk.Frame(frame3, borderwidth=2, relief="solid")
content_f3.place(relx=0.2, y=0, relwidth=0.8, relheight=1)

schedule_title = ttk.Label(content_f3, text="weekly schedule", font=("Arial", 25, "bold"))
schedule_title.pack(pady=(30, 20))

inner_frame3 = ttk.Frame(content_f3, borderwidth=2, relief="solid")
inner_frame3.pack(fill=BOTH, expand=True, padx=40, pady=(0, 40))

day_label = ttk.Label(inner_frame3, text="Select Day:", font=("Arial", 15, "bold"))
day_label.pack(pady=(20, 5))

days_of_week = list(WEEKLY_SCHEDULE.keys())
day_combobox = ttk.Combobox(inner_frame3, values=days_of_week, state="readonly", font=("Arial", 15))
day_combobox.pack(pady=5)
try:
    day_combobox.set(datetime.now().strftime("%A"))
except:
    day_combobox.set("Monday")

#--------------------------SCHEDULE TABLE--------------------------------
full_columns = ("subject", "professor", "time")
full_sched_table = ttk.Treeview(inner_frame3, columns=full_columns, show="headings", height=15)
full_sched_table.heading("subject", text="SUBJECT CODE")
full_sched_table.heading("professor", text="PROFESSOR")
full_sched_table.heading("time", text="SCHEDULED TIME")
full_sched_table.column("subject", width=250, anchor=CENTER)
full_sched_table.column("professor", width=350, anchor=CENTER)
full_sched_table.column("time", width=350, anchor=CENTER)
full_sched_table.pack(pady=20, fill=BOTH, expand=True, padx=20)

def update_full_schedule(event=None):
    selected_day = day_combobox.get()
    for item in full_sched_table.get_children():
        full_sched_table.delete(item)
    
    classes = WEEKLY_SCHEDULE.get(selected_day, [])
    for subject, prof, time in classes:
        full_sched_table.insert("", END, values=(subject, prof, time))

day_combobox.bind("<<ComboboxSelected>>", update_full_schedule)
# Initial population
update_full_schedule()

######################## GRADES PAGE (Frame 4)
create_sidebar(frame4)

update_dashboard_data()
show_frame(frame1)
window.mainloop()