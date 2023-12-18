from flask import Flask, render_template, request, redirect, url_for
import webbrowser
import os
import csv
app = Flask(__name__)

# Predefined login credentials
predefined_credentials = {
    "John": {"class": "11", "section": "A", "password": "123", "role": "teacher"},
    "Jane": {"class": "10", "section": "B", "password": "456", "role": "student"},
    "Meet": {"class": "11", "section": "A", "password": "122", "role": "student"},
    "Admin": {"class": 'x', "section": 'x', "password": "Admin", "role": "admin"},

}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    # Open the specified URL when signing up
    webbrowser.open("https://bard.google.com/chat")
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        class_ = request.form['class']
        sec = request.form['section']
        password = request.form['password']

        print(f"Received form data - Name: {name}, Class: {class_}, Section: {sec}, Password: {password}")

        if name in predefined_credentials:
            predefined_data = predefined_credentials[name]

            # Check if the user is an admin
            if predefined_data.get("role") == "admin":
                print("User is an admin.")
                if password == predefined_data.get("password"):
                    print("Admin login successful.")
                    return redirect(url_for('main_page', role=predefined_data.get("role")))
                else:
                    print("Admin login failed.")
                    error_message = "Invalid credentials. Please try again."
                    return render_template('login.html', error_message=error_message)

            # For other roles, validate Class and Section
            elif (
                class_ == predefined_data.get("class", "") and
                sec == predefined_data.get("section", "") and
                password == predefined_data.get("password", "")
            ):
                print("User is not an admin. Class and Section validation passed.")
                return redirect(url_for('main_page', role=predefined_data.get("role")))
            else:
                print("User is not an admin. Class and Section validation failed.")
                error_message = "Invalid credentials. Please try again."
                return render_template('login.html', error_message=error_message)

        else:
            print("User not found.")
            error_message = "User not found. Please try again."
            return render_template('login.html', error_message=error_message)

    return render_template('login.html', error_message=None)

@app.route('/admin_main_page')
def admin_main_page():
    return render_template('admin_main_page.html')

@app.route('/main_page/<role>')
def main_page(role):
    return render_template('main_page.html', role=role)

app = Flask(__name__)

# Function to check user credentials and determine the user role
def check_credentials(username, password):
    predefined_credentials = {
        "John": {"class": "11", "section": "A", "password": "123", "role": "teacher"},
    }

    if username in predefined_credentials and password == predefined_credentials[username]["password"]:
        return predefined_credentials[username]["role"]
    else:
        return None

# Initialize user role
user_role = None

# Route for the teacher dashboard
@app.route('/teacher_dashboard')
def teacher_dashboard():
    global user_role
    if user_role != "teacher":
        return redirect(url_for('login'))

    return render_template('teacher_dashboard.html')

# Route for handling assignment upload by the teacher
@app.route('/upload_assignment', methods=['POST'])
def upload_assignment():
    global user_role
    if user_role != "teacher":
        return redirect(url_for('login'))

    file_path = request.files['file']
    if file_path:
        # Check if the file is a PDF or PNG
        if file_path.filename.endswith((".pdf", ".png")):
            # Determine the destination path in the "Assignments" folder
            destination_folder = "static/Assignments"
            destination_path = os.path.join(destination_folder, file_path.filename)

            # Save the file to the "Assignments" folder
            try:
                os.makedirs(destination_folder, exist_ok=True)
                file_path.save(destination_path)
                return "Assignment uploaded successfully."
            except Exception as e:
                return f"An error occurred: {str(e)}"
        else:
            return "Only PDF and PNG files are allowed."
    else:
        return "File not provided."

app = Flask(__name__)

app = Flask(__name__)

# Function to save an announcement to the CSV file
def save_announcement(announcement):
    with open('announcements.csv', 'a', newline='') as file:
        file.write(announcement + '\n')

# Function to retrieve announcements from the CSV file
def get_announcements():
    announcements = []
    try:
        with open('announcements.csv', 'r') as file:
            announcements = file.read().splitlines()
    except FileNotFoundError:
        pass  # Handle the case when the file is not found
    return announcements

# Function to display announcements
def display_announcements():
    announcements = get_announcements()
    return announcements

# Function to make a new announcement
def make_announcement(announcement):
    save_announcement(announcement)

# Routes
@app.route('/')
def index():
    announcements = display_announcements()
    return render_template('index.html', announcements=announcements)

@app.route('/make_announcement', methods=['POST'])
def make_announcement_route():
    announcement = request.form['announcement']
    make_announcement(announcement)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
