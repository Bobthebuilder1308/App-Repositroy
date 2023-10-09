import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import webbrowser
import os
import sqlite3

# Create the main window
window = tk.Tk()
window.title("Teacher Dashboard")
window.geometry("800x600")
window.configure(bg="khaki1")

# Initialize user role
user_role = None

# Predefined login credentials
predefined_credentials = {
    "John": {"class": "11", "section": "A", "password": "123", "role": "teacher"},
}
# Create a directory to store uploaded assignments
upload_dir = os.path.expanduser("~")
# Function to handle assignment upload by the teacher
def upload_assignment():
    file_path = filedialog.askopenfilename(title="Upload Assignment", filetypes=[("PDF Files", "*.pdf"), ("PNG Files", "*.png")])

    if file_path:
        # Check if the file is a PDF or PNG
        if file_path.endswith((".pdf", ".png")):
            # Save the assignment file to the "Assignments" folder
            assignment_filename = os.path.basename(file_path)
            save_path = os.path.join("Assignments", assignment_filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            os.replace(file_path, save_path)
            # Allow the teacher to provide separate instructions
            instruction = simpledialog.askstring("Assignment Instructions", "Enter assignment instructions (optional):")
            # Display the instructions in a messagebox
            if instruction:
                messagebox.showinfo("Assignment Instructions", instruction)
            else:
                messagebox.showinfo("Assignment Instructions", "No additional instructions provided.")
        else:
            messagebox.showerror("Invalid File", "Only PDF and PNG files are allowed.")


# Function to show teacher options
def show_teacher_options():
    def on_announcements():
        pass

    def on_my_timetable():
        my_timetable_page()

    def on_create_test():
        create_test()

    def on_check_grade():
        check_grade()

    def on_assignments():
        teacher_assignments_page()

    button_width = 20
    button_height = 3

    # Create buttons for various options
    announcements_button = tk.Button(window, text="Announcements", command=on_announcements,
                                     bg="firebrick1", fg="white", font=("Arial", 16), width=button_width, height=button_height)
    announcements_button.grid(row=1, column=1, padx=(40, ))

    my_timetable_button = tk.Button(window, text="My Timetable", command=on_my_timetable,
                                   bg="cyan3", fg="white", font=("Arial", 16), width=button_width, height=button_height)
    my_timetable_button.grid(row=1, column=2, padx=10)

    create_test_button = tk.Button(window, text="Create Test", command=on_create_test,
                                   bg="tomato", fg="white", font=("Arial", 16), width=button_width, height=button_height)
    create_test_button.grid(row=1, column=3, padx=(10, 50))

    check_grade_button = tk.Button(window, text="Check Student Grade", command=on_check_grade,
                                   bg="red4", fg="white", font=("Arial", 16), width=button_width, height=button_height)
    check_grade_button.grid(row=1, column=4, padx=(50, 10))

    assignments_button = tk.Button(window, text="Assignments", command=upload_assignment,
                                   bg="lawn green", fg="white", font=("Arial", 16), width=button_width, height=button_height)
    assignments_button.grid(row=1, column=5, padx=(10, 50))

# Show teacher options without the need for a button
show_teacher_options()

# Function For Teacher's Create Test
def create_test():
    webbrowser.open("https://quizizz.com/?lng=en")

# Function for Teacher's Assignments Page
def teacher_assignments_page():
    # Create the teacher's assignments page window
    assignments_window = tk.Toplevel(master=window)
    assignments_window.title("Teacher's Assignments")
    assignments_window.geometry("800x600")
    assignments_window.configure(bg="light green")
    assignments_window.grab_set()
    tk.Label(assignments_window, text="Teacher's Assignments", font=("Arial", 18), bg="light green").pack(pady=10)

# Function to check student grade
def check_grade():
    messagebox.showinfo("Work in Progress", "Feature coming soon.")

# Function for My Timetable Page
def my_timetable_page():
    messagebox.showinfo("Work in Progress", "Feature coming soon.")

# Start the main event loop
window.mainloop()
