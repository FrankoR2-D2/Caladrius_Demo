from django.db import models
# from django.contrib.auth.models import User 
from django.conf import settings
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class ToDoList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    
    def __str__(self):
        return self.text



class Doctor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    SPEC_CHOICES = (
        ("General Practioner", "General Practioner"),
        ("Anesthesiologists", "Anesthesiologists"),
        ("Dermatologists", "Dermatologists"),
        ("Family Physician", "Family Physician"),
        ("Internists", "Internists"),
        ("Pediatrician", "Pediatrician"),
        ("Radiologists", "Radiologists"),
        ("Cardiologist", "Cardiologist"),
        ("Audiologist", "Audiologist"),
    )
    specialization = models.CharField(max_length=300, choices=SPEC_CHOICES, default="GP")
    
    def __str(self):
        return str(f'Dr. {self.user}, {self.specialization}')

class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="addPatient", null=True)
    patientNotes = models.CharField(max_length=300)
    
    def __str(self):
        return str(f'{self.user}, {self.priotity} ')

class Appointments(models.Model):
    start_time = models.TimeField('Start time', null=True)
    end_time = models.TimeField('End time', null=True)
    date = models.DateField('Date', null=True)
    status = models.BooleanField('Appointment Status', null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, default = None, related_name="appDoctor")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True, default = None, related_name="appPatient")
    appointment_reason = models.TextField(null=True)
    
    def __str(self):
        return str(f'{self.date}, {self.start_time}, {self.end_time}, {self.status}, {self.patient}, {self.doctor}, {self.appointment_reason}')
    


