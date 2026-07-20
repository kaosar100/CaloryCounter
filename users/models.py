from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PersonalInfo(models.Model):
    sex_choice = [
        ('male', 'male'),
        ('female', 'female')
    ]
    
    activity_choice = [
         ("Sedentary", "Sedentary"),
        ("Light", "Light"),
        ("Moderate", "Moderate"),
        ("Active", "Active"),
        ("Very Active", "Very Active"),
    ]
    
    goal_choice = [
        ("Lose Weight", "Lose Weight"),
        ("Maintain Weight", "Maintain Weight"),
        ("Gain Weight", "Gain Weight"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10, choices=sex_choice)
    height = models.FloatField(help_text='height in centimeter')
    weight = models.FloatField(help_text='weight in kilogram')
    activity_level = models.CharField(max_length=20, choices=activity_choice)
    
    goal = models.CharField(max_length=20, choices=goal_choice)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username