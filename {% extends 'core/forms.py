from django import forms
from .models import Patient, Vitals, BloodTest, BMI, ECG, Ultrasound

SYMPTOMS_CHOICES = [('cough','Cough'),('fever','Fever'),('fatigue','Fatigue')]  # extend as needed

class PatientForm(forms.ModelForm):
    symptoms = forms.MultipleChoiceField(choices=SYMPTOMS_CHOICES, widget=forms.CheckboxSelectMultiple)
    consent = forms.BooleanField(label="I consent per NDHM/WHO")

    class Meta:
        model = Patient
        fields = ['full_name','age','gender','patient_id','contact','address','geo_code','family_history','symptoms','consent']

class VitalsForm(forms.ModelForm):
    class Meta:
        model = Vitals
        fields = ['bp_systolic','bp_diastolic','heart_rate','temperature','spo2']

class BloodTestForm(forms.ModelForm):
    class Meta:
        model = BloodTest
        fields = ['hemoglobin','blood_sugar','hdl','ldl','tc','tg']

class BMIForm(forms.ModelForm):
    class Meta:
        model = BMI
        fields = ['height_cm','weight_kg']

class ECGForm(forms.ModelForm):
    class Meta:
        model = ECG
        fields = ['heart_rate','qrs_duration','qt_interval','waveform_data']

class UltrasoundForm(forms.ModelForm):
    class Meta:
        model = Ultrasound
        fields = ['image','observation']
