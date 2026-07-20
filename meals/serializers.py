from rest_framework import serializers
from .models import Meal

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = (
            'id',
            'food_name',
            'meal_type',
            "quantity",
            'calory',
            'protein',
            'carbs',
            'fat',
            'meal_date',
            'created_at',
            'updated_at',
            
        )
        
        read_only_fields=(
            "id",
            "created_at",
            "updated_at",
        )