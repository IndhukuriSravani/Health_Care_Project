from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
    language = models.CharField(max_length=20, choices=[('en', 'English'), ('hi', 'Hindi'), ('te', 'Telugu')], default='en')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
