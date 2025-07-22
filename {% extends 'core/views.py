from .forms import *
from .models import *
from django.utils import timezone
from django.shortcuts import get_object_or_404
import io, base64, matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import qrcode
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

@login_required
def wizard_page(request, visit_id, step):
    visit = get_object_or_404(Visit, id=visit_id)
    form_classes = {
        1: PatientForm, 2: VitalsForm, 3: BloodTestForm, 4: BMIForm, 5: ECGForm, 6: UltrasoundForm
    }
    model_map = {
        1: Patient, 2: Vitals, 3: BloodTest, 4: BMI, 5: ECG, 6: Ultrasound
    }

    Form = form_classes[step]
    instance = model_map[step].objects.filter(visit=visit).first()
    form = Form(request.POST or None, request.FILES or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        obj = form.save(commit=False)
        obj.visit = visit
        obj.save()
        next_step = step + 1
        return redirect('wizard', visit_id=visit.id, step=next_step)
    return render(request, f'core/wizard_step{step}.html', {'form': form, 'step': step, 'visit': visit})

def finalize_visit(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    # -- Risk scoring algorithm
    score = 0
    vitals = visit.vitals
    if vitals.bp_systolic > 140 or vitals.bp_diastolic > 90: score += 20
    if vitals.heart_rate > 100 or vitals.heart_rate < 60: score += 10
    blood = visit.bloodtest
    if blood.blood_sugar > 140: score += 15
    bmi = visit.bmi.bmi_value()
    if bmi > 30: score += 20
    ecg_summary = visit.ecg.summary()
    if "Arrhythmia" in ecg_summary: score += 20
    visit.summary = ecg_summary
    visit.risk_score = min(score, 100)
    visit.risk_band = ('Low' if score<40 else 'Medium' if score<70 else 'High')
    visit.save()
    return redirect('download_report', visit_id=visit.id)

def download_report(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    # Header + logo
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, 750, "Clinic Name – Healthcare on Wheels")
    p.drawImage("static/img/logo.png", 450, 730, width=100, height=50)
    # Patient and vitals data...
    p.drawString(50, 700, f"Patient: {visit.patient.full_name} | Risk Score: {visit.risk_score}")
    # ECG plot image
    ecg = visit.ecg
    fig, ax = plt.subplots()
    ax.plot(ecg.get_waveform())
    plt.title("ECG")
    imgbuf = io.BytesIO()
    fig.savefig(imgbuf, format='PNG')
    imgbuf.seek(0)
    p.drawImage(imgbuf, 50, 500, width=500, height=200)
    # QR linking
    qr = qrcode.make(request.build_absolute_uri(reverse('visit_detail', args=[visit.id])))
    qr_io = io.BytesIO()
    qr.save(qr_io)
    qr_io.seek(0)
    p.drawImage(qr_io, 50, 450, width=100, height=100)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"report_{visit.id}.pdf")
