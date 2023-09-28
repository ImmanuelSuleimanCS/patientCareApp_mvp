from flask import Flask, render_template, request, redirect, url_for
from models import db, Patient, DailyInfo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'

db.init_app(app)


@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/initial', methods=['GET', 'POST'])
def initial():
    if request.method == 'POST':
        # Extract data from form
        name = request.form.get('name')
        dob = request.form.get('dob')
        gender = request.form.get('gender')
        admit_date = request.form.get('admit_date')
        # Add more fields as necessary...

        # Create a new Patient object and add to the database
        new_patient = Patient(name=name, dob=dob,
                              gender=gender, admit_date=admit_date)
        db.session.add(new_patient)
        db.session.commit()

        # Redirect to the landing page after adding
        return redirect(url_for('index'))

    return render_template('initial.html')


@app.route('/daily', methods=['GET', 'POST'])
def daily():
    patients = Patient.query.all()
    if request.method == 'POST':
        # Extract data from form
        patient_id = request.form.get('patient_id')
        vital_signs = request.form.get('vital_signs')
        medications = request.form.get('medications')
        needs = request.form.get('needs')
        notes = request.form.get('notes')
        # Add more fields as necessary...

        # Create a new DailyInfo object and add to the database
        daily_info = DailyInfo(patient_id=patient_id, vital_signs=vital_signs,
                               medications=medications, needs=needs, notes=notes)
        db.session.add(daily_info)
        db.session.commit()

        # Redirect to the same page (or elsewhere if desired) after adding
        return redirect(url_for('daily'))

    return render_template('daily.html', patients=patients)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # Creates the database tables if they don't exist
    app.run(debug=True)
