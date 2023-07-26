from django.contrib import admin
from .models import (PatientModel, DepartmentModel, AppointmentModel, 
                    Medical_ReccordModel,  DoctorModel, StaffModel, CustomUser)
from .forms import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(DoctorModel)
admin.site.register(PatientModel)
admin.site.register(StaffModel)
admin.site.register(Medical_ReccordModel)
admin.site.register(DepartmentModel)
admin.site.register(AppointmentModel)
