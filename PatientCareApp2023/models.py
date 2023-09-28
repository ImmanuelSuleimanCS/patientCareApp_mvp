from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    dob = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    admit_date = db.Column(db.String(10))

class DailyInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    vitals = db.Column(db.String(200))
    medications = db.Column(db.String(200))
    needs = db.Column(db.String(200))
    notes = db.Column(db.String(500))
