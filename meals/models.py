from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meal(models.Model):
    meal_choices = [
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snacks', 'snacks'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='meals'
    )
    
    meal_type = models.CharField(max_length=20, choices=meal_choices)
    food_name = models.CharField(max_length=100)
    quantity = models.FloatField()
    calory = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    meal_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.food_name}"
    
    
    
    