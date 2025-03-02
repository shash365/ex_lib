# ex_lib
UI

### Steps -

# 1. Clone the repo

```bash
    git clone httpsPATH
```

# 2. Create virtual env

```bash
    python -m venv "virtual environment name"
#    conda create -n venvel python=3.8 -y
```

# 3. Activate virtual env

to activate on Windows
```bash
   .\venvel\Scripts\activate
```
## venvel is the virtual env name
to activate in MacOS or Linux
```bash
   source venvel/bin/activate
```
### for our project, activate file is present in path - venvel->Scripts->activate
### so command will be -  source venvel/Scripts/activate

```bash
#    conda activate venvel
```

### After activation, your terminal prompt should change (typically showing (venv)), indicating that the virtual environment is active. Now, any packages you install will be isolated to this environment. ###

# 4. Install requirements

```bash
    pip install -r requirements.txt
```

# 5. Add installed requirements to a file
pip freeze > req.txt

# 6. File structure of this project 
Flask-Student-App/
│── app.py                 # Main Flask application
│── requirements.txt        # Dependencies file
│── students.csv            # CSV file to store student details (auto-created)
│── venv/                   # Virtual environment (optional, not pushed to GitHub)
│── templates/              # HTML Templates folder
│   │── index.html          # Form to add students
│   │── students.html       # Display students list
│── static/                 # (Optional) For CSS, JavaScript, images
│── .gitignore              # Git ignore file


# 7. .gitignore file
Contains virtual env, csv and other files to be ignored

# 8. To run Flask app
python app.py

# 9. Access Web App
http://127.0.0.1:5000/

