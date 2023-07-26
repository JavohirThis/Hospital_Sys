from django import forms 
from hospital.models import *
class PersonForms(forms.ModelForm):
    first_name_uz = forms.CharField
    first_name_ru = forms.CharField
    first_name_en = forms.CharField
    last_name_uz = forms.CharField
    last_name_ru = forms.CharField
    last_name_en = forms.CharField
    email_uz = forms.CharField
    email_ru = forms.CharField
    email_en = forms.CharField
class Meta:
    model = PersonModel
class DepartmentForms(forms.ModelForm):
    name_uz = forms.CharField
    name_ru = forms.CharField
    name_en = forms.CharField
    description_uz = forms.CharField
    description_ru = forms.CharField
    description_en = forms.CharField
class Meta:
    model = DepartmentModel
class DoctorForms(forms.ModelForm):
    specialization_uz = forms.CharField
    specialization_ru = forms.CharField
    specialization_en = forms.CharField
    degree_uz = forms.CharField
    degree_ru = forms.CharField
    degree_en = forms.CharField
    department_uz = forms.CharField
    department_ru = forms.CharField
    department_en = forms.CharField
class Meta:
    model = DoctorModel
class PatientForms(forms.ModelForm):
    medical_history_uz = forms.CharField
    medical_history_ru = forms.CharField
    medical_history_en = forms.CharField
    assigned_doctor_uz = forms.CharField
    assigned_doctor_ru = forms.CharField    
    assigned_doctor_en = forms.CharField 
    illness_uz = forms.CharField
    illness_ru = forms.CharField
    illness_en = forms.CharField
class Meta:
    model = PatientModel
class StaffForms(forms.ModelForm):
    department_uz = forms.CharField
    department_ru = forms.CharField
    department_en = forms.CharField
    job_uz = forms.CharField
    job_ru = forms.CharField
    job_en = forms.CharField
class Meta:
    model = StaffModel
class Medical_ReccordForms(forms.ModelForm):
    patient_uz = forms.CharField
    patient_ru = forms.CharField
    patient_en = forms.CharField
    diagnosis_uz = forms.CharField
    diagnosis_ru = forms.CharField
    diagnosis_en = forms.CharField
    treatment_uz = forms.CharField
    treatment_ru = forms.CharField
    treatment_en = forms.CharField
class Meta:
    model = Medical_ReccordModel
class AppointmentForms(forms.ModelForm):
    doctor_uz = forms.CharField
    doctor_ru = forms.CharField
    doctor_en = forms.CharField
    patient_uz = forms.CharField
    patient_ru = forms.CharField
    patient_en = forms.CharField
class Meta:
    model = AppointmentModel
class PrescriptionForms(forms.ModelForm):
    doctor_uz = forms.CharField
    doctor_ru = forms.CharField
    doctor_en = forms.CharField
    patient_uz = forms.CharField
    patient_ru = forms.CharField
    patient_en = forms.CharField
    medication_uz = forms.CharField
    medication_ru = forms.CharField
    medication_en = forms.CharField
    dosage_uz = forms.CharField
    dosage_ru = forms.CharField
    dosage_en = forms.CharField
    instructions_uz = forms.CharField
    instructions_ru = forms.CharField
    instructions_en = forms.CharField