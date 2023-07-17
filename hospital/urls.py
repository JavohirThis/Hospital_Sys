from django.urls import path
from .views import (PersonView, PersonDetailView, PatientView,PatientDetailView, 
                    DoctorView, DoctorDetailView, PrescriptionView, PrescriptionDetailView, 
                    AppointmentView, AppointmentDetailView, Medical_ReccordView, Medical_ReccordDetailView,
                    StaffView,  StaffDetailView, DepartmentView, DepartmentDetailView)

urlpatterns = [
    path('person/', PersonView.as_view()),
    path('person/<pk>/', PersonDetailView.as_view()),
    path('doctor/', DoctorView.as_view()),
    path('doctor/<pk>/', DoctorDetailView.as_view()),
    path('patient/', PatientView.as_view()),
    path('patient/<pk>/', PatientDetailView.as_view()),
    path('prescription/', PrescriptionView.as_view()),
    path('prescription/<pk>/', PrescriptionDetailView.as_view()),
    path('appointment/', AppointmentView.as_view()),
    path('appointment/<pk>/', AppointmentDetailView.as_view()),
    path('medical_reccord/', Medical_ReccordView.as_view()),
    path('medical_reccord/<pk>/', Medical_ReccordDetailView.as_view()),
    path('staff/', StaffView.as_view()),
    path('staff/<pk>/', StaffDetailView.as_view()),
    path('department/', DepartmentView.as_view()),
    path('department/<pk>/', DepartmentDetailView.as_view())
]