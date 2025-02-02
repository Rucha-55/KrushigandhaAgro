from django.db import models
from django.utils import timezone
class Carrier(models.Model):
    POST_CHOICES = [
        ('Senior Accountant', 'Senior Accountant'),
        ('Marketing Manager', 'Marketing Manager'),
        ('Junior Accountant', 'Junior Accountant'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    # Job-related fields
    post = models.CharField(max_length=100, choices=POST_CHOICES)
    experience = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')

    # Timestamp field
    created_at = models.DateTimeField(default=timezone.now)  # Set a default value using timezone.now
    def __str__(self):
        return self.name
