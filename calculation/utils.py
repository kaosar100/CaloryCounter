def calculate_bmr(profile):
    if profile.sex.lower() == "male":
        return (
            (10 * profile.weight)
            + (6.25 * profile.height)
            - (5 * profile.age)
            + 5
        )

    return (
        (10 * profile.weight)
        + (6.25 * profile.height)
        - (5 * profile.age)
        - 161
    )
    

def calculate_tdee(profile):
    
    
    activity_multiplier = {

        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Active": 1.725,
        "Very Active": 1.9,

    }
    
    bmr = calculate_bmr(profile)
    
    return bmr*activity_multiplier[profile.activity_level]

def target_calories(profile):
    tdee = calculate_tdee(profile)
    
    if profile.goal == 'Lose Weight':
        return tdee - 500
    elif profile.goal == 'Gain Weight':
        return tdee + 500
    else:
        return tdee

from meals.models import Meal
from datetime import date

def calories_consumed_today(user):
    meals = Meal.objects.filter(user=user, meal_date=date.today())
    total = sum(meal.calory for meal in meals)
    
    return total


def remaining_calories(profile):
    target = target_calories(profile)
    consumed = calories_consumed_today(profile.user)
    
    return target-consumed 
    