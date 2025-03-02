from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)
CSV_FILE = "students.csv"

# Ensure CSV file exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Grade", "Email"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']
    email = request.form['email']
    
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade, email])
    
    return redirect(url_for('index'))

@app.route('/students')
def list_students():
    students = []
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        students = [row for row in reader]
    
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
