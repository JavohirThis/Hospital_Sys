from modeltranslation.translator import translator, TranslationOptions,register
from hospital.models import *

@register(PersonModel)
class PersonTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'email', 'adress')
@register(DepartmentModel)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(DoctorModel)
class DoctorTranslationOptions(TranslationOptions):
    fields = ('specialization', 'degree', 'department')

@register(PatientModel)
class PatientTranslationOptions(TranslationOptions):
    fields = ('medical_history', 'assigned_doctor','illness')

@register(StaffModel)
class StaffTranslationOptions(TranslationOptions):
    fields = ('department', 'job')
    
@register(Medical_ReccordModel)
class Meedical_RecordTranslationOptions(TranslationOptions):
    fields = ('patient', 'diagnosis', 'treatment')

@register(AppointmentModel)
class AppointmentTranslationOptions(TranslationOptions):
    fields = ('doctor', 'patient')

@register(PrescriptionModel)
class PrescriptionTranslationOptions(TranslationOptions):
    fields = ('doctor', 'patient', 'medication', 'dosage', 'instructions')