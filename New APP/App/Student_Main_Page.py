import customtkinter as ctk
from customtkinter import CTkButton,CTkToplevel,CTkLabel,CTkFrame,CTk
import os
import shutil
import subprocess
'''
# Sample assignment data
assignments = [
    {"name": "Assignment 1", "file_path": "assignment1.pdf"},
    {"name": "Assignment 2", "file_path": "assignment2.png"},
]'''
# Function to show a custom message box
def show_message(title, message):
    message_box = ctk.CTkToplevel()
    message_box.title(title)
    message_box.geometry("400x150")
    message_box.configure(bg_color="light blue")
    message_label = ctk.CTkLabel(message_box, text=message)  # Create label without font
    message_label.pack(pady=20)
    message_label.configure(font=("Arial", 14))
    ok_button = ctk.CTkButton(message_box, text="OK", command=message_box.destroy)
    ok_button.pack()
    # Center the message box on the screen
    message_box.update_idletasks()
    x = (message_box.winfo_screenwidth() - message_box.winfo_reqwidth()) / 2
    y = (message_box.winfo_screenheight() - message_box.winfo_reqheight()) / 2
    message_box.geometry(f"+{int(x)}+{int(y)}")

def view_global_announcement():
    subprocess.run(['python', r'New APP\App\View Global Announcement.py'], check=True)

# Function displays "Feature coming soon" message
def feature_coming_soon():
    show_message("Feature Coming Soon", "This feature is coming soon.")
# Function opens file dialog for assignment download
def download_assignment(file_path):
    save_path = ctk.filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=os.path.basename(file_path))
    if save_path:
        shutil.copyfile(file_path, save_path)
        show_message("Download Assignment", f"Downloading {os.path.basename(file_path)} to {save_path}")
# Function lists assignments in "Assignments" folder
def list_assignments():
    assignments_folder = "Assignments"
    assignments = []
    if os.path.exists(assignments_folder):
        assignment_files = os.listdir(assignments_folder)
        for file_name in assignment_files:
            assignment = {"name": file_name, "file_path": os.path.join(assignments_folder, file_name)}
            assignments.append(assignment)
    return assignments
# Function displays and manages assignment list
def view_assignments():
    assignments = list_assignments()
    if assignments:
        assignments_window = CTkToplevel(student_window)
        assignments_window.title("Assignments")
        assignments_window.geometry("800x600")
        content_frame = CTkFrame(assignments_window)
        content_frame.pack(pady=20, padx=10)
        for i, assignment in enumerate(assignments):
            assignment_label = CTkLabel(content_frame, text=f"{i + 1}. {assignment['name']}", font=("Arial", 16))
            assignment_label.pack(pady=10)
            download_button = CTkButton(content_frame, text="Download", command=lambda path=assignment["file_path"]: download_assignment(path))
            download_button.pack()
    else:
        message_box = CTkToplevel(student_window)
        message_box.title("No Assignments")
        message_label = CTkLabel(message_box, text="There are no assignments available.", font=("Arial", 16))
        message_label.pack(pady=20)
        message_box.focus_force()
# Create student profile window
student_window = CTk()
student_window.title("Student Profile")
student_window.geometry("800x600")

# Create and place buttons using CTkButton
announcements_button = CTkButton(
    student_window, text="Announcements", command=view_global_announcement, 
    bg_color="red2", text_color="white", font=("Arial", 16)
)
assignments_button = CTkButton(
    student_window, text="Assignments", command=view_assignments, 
    bg_color="dodger blue", text_color="white", font=("Arial", 16)
)

timetable_button = CTkButton(
    student_window, text="My Class Timetable", command=feature_coming_soon, 
    bg_color="green4", text_color="white", font=("Arial", 16)
)

grade_button = CTkButton(
    student_window, text="Check My Grade", command=feature_coming_soon, 
    bg_color="dark orchid", text_color="white", font=("Arial", 16)
)

profile_button = CTkButton(
    student_window, text="Profile", command=feature_coming_soon, 
    bg_color="hot pink", text_color="white", font=("Arial", 12)
)

announcements_button.pack(pady=20)
assignments_button.pack(pady=20)
timetable_button.pack(pady=20)
grade_button.pack(pady=20)
# Start main event loop for student profile window
student_window.mainloop()
