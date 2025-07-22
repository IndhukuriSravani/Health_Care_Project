class Patient(models.Model):
    visit = models.OneToOneField('Visit', on_delete=models.CASCADE, related_name='patient')
    # same fields as form...

class Visit(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    summary = models.TextField(blank=True)
    risk_score = models.IntegerField(default=0)
    risk_band = models.CharField(max_length=10, blank=True)

class Vitals(models.Model):
    visit = models.OneToOneField(Visit, on_delete=models.CASCADE, related_name='vitals')
    # fields...
    def is_abnormal(self):
        return self.bp_systolic >140 or self.heart_rate>100

# Similar: BloodTest, BMI (with method calculate bmi), ECG (with summary and waveform stored as JSON/MS blob), Ultrasound...
