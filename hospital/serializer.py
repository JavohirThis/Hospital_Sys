from rest_framework import serializers
from .models import PersonModel, PatientModel, DoctorModel, PrescriptionModel, AppointmentModel, Medical_ReccordModel, DepartmentModel, StaffModel
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = '__all__'
    
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientModel
        fields = '__all__'
    
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorModel
        fields = '__all__'
    
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionModel
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentModel
        fields = '__all__'

class Medical_ReccordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical_ReccordModel
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffModel
        fields = '__all__'