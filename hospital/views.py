from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import PersonModel, PatientModel, DoctorModel, PrescriptionModel, AppointmentModel, Medical_ReccordModel, DepartmentModel, StaffModel
from .serializer import (PatientSerializer, PersonSerializer, DoctorSerializer, StaffSerializer,
                         PrescriptionSerializer, AppointmentSerializer, Medical_ReccordSerializer, DepartmentSerializer)

class PersonView(generics.ListCreateAPIView):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer
    
class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer

class DoctorView(generics.ListCreateAPIView):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializer

class PrescriptionView(generics.ListCreateAPIView):
    queryset = PrescriptionModel.objects.all()
    serializer_class = PrescriptionSerializer

class PrescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrescriptionModel.objects.all()
    serializer_class = PrescriptionSerializer

class PatientView(generics.ListCreateAPIView):
    queryset = PatientModel.objects.all()
    serializer_class = PatientSerializer

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientModel.objects.all()
    serializer_class = PatientSerializer

class AppointmentView(generics.ListCreateAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer

class Medical_ReccordView(generics.ListCreateAPIView):
    queryset = Medical_ReccordModel.objects.all()
    serializer_class = Medical_ReccordSerializer

class Medical_ReccordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medical_ReccordModel.objects.all()
    serializer_class = Medical_ReccordSerializer

class DepartmentView(generics.ListCreateAPIView):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer

class StaffView(generics.ListCreateAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffSerializer

class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffSerializer







