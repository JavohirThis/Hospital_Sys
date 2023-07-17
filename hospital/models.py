from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','Admin'),
        ('d','Doctor'),
        ('s','Stuff')
    )
    roles =     models.CharField(max_length=1,choices=ROLE_CHOICES)


class PersonModel(models.Model):
    custum = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, default=None)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    phone_number = PhoneNumberField(blank = True)
    email = models.EmailField(max_length=100, blank= True)
    gender = models.CharField(max_length=20, default='')
    class Age(models.Model):
        birth_date = models.DateField()
    def get_age(self):
        age = datetime.date.today()-self.birth_date
        return int((age).days/365.25)
    adress = models.CharField(max_length=200, default='')
    created_at = models.DateTimeField(default= datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = 'person'

class DepartmentModel(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=3000, default='') 
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'department'

class DoctorModel(PersonModel):
    specialization = models.CharField(max_length=50, default='')
    degree = models.CharField(max_length=50, default='')
    availability_status = models.BooleanField(default=True)
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.specialization}"
    
    class Meta:
        db_table = 'doctor'

class PatientModel(PersonModel):
    medical_history = models.CharField(max_length=9999, default='')
    assigned_doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    illness = models.CharField(max_length=200, default='')
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = 'patient'

class StaffModel(PersonModel):
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    job = models.CharField(max_length=99, default='')
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.job}"
    
    class Meta:
        db_table = 'staff'

class Medical_ReccordModel(models.Model):
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=3030, default='')
    treatment = models.CharField(max_length=2023, default='')
    def __str__(self) -> str:
        return f"{self.patient} {self.diagnosis}"
    
    class Meta:
        db_table = 'medical'

class AppointmentModel(models.Model):
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    A_time = models.DateTimeField(default=datetime)
    A_date = models.DateField(default=datetime)
    def __str__(self) -> str:
        return f"{self.doctor} {self.patient}"
    
    class Meta:
        db_table = 'appointment'

class PrescriptionModel(models.Model):
    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    medication = models.CharField(max_length=299, default='')
    dosage = models.CharField(max_length=123, default='')
    instructions = models.CharField(max_length=1234, default='')
    def __str__(self) -> str:
        return f"{self.doctor} {self.patient} {self.medication}"
    
    class Meta:
        db_table = 'prescription'