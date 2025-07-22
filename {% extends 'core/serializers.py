from rest_framework import serializers
from .models import Patient, Visit, ECG

class PatientSerializer(serializers.ModelSerializer):
    class Meta: model = Patient; fields = '__all__'

class VisitSerializer(serializers.ModelSerializer):
    class Meta: model = Visit; fields = '__all__'

class ECGSerializer(serializers.ModelSerializer):
    class Meta: model = ECG; fields = '__all__'
