
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# class UserData(models.Model):
#     MALE = 'M'
#     FEMALE = 'F'
#     PREFER_NOT_TO_SAY = 'N'

#     GENDER_CHOICES = [
#         (MALE, 'Male'),
#         (FEMALE, 'Female'),
#         (PREFER_NOT_TO_SAY, 'Prefer not to say'),
#     ]

#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     gender = models.CharField(
#         max_length=1,
#         choices=GENDER_CHOICES,
#         default=PREFER_NOT_TO_SAY,
#     )
#     email = models.EmailField()

#     def __str__(self):
#         return self.name
    
# class SleepData(models.Model):
#     username = models.CharField(max_length=255)
#     sleep_duration = models.IntegerField()  # Hours of sleep
#     quality_of_sleep = models.IntegerField()  # Rating (e.g., 1 to 5)
#     stress_level = models.IntegerField()  # Stress level (e.g., 1 to 5)
    
#     def __str__(self):
#         return f"SleepData for {self.username}"

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True, related_name='userdata')

    # Page 1
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)
    physical_activity_level = models.CharField(max_length=20)

    # Page 2
    sleep_hours = models.IntegerField()
    quality_of_sleep = models.IntegerField()
    stress_level = models.CharField(max_length=20)

    # Page 3
    height = models.FloatField()
    weight = models.FloatField()

    # Page 4
    blood_pressure_category = models.CharField(max_length=30)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()

    # Page 5
    heart_rate = models.IntegerField()
    daily_steps = models.IntegerField()
    sleep_disorder = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user.username}'s health data"