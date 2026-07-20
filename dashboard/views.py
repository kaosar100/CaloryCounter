from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import date
from users.models import PersonalInfo
from meals.models import Meal
from calculation.utils import (
    calculate_bmr,
    calculate_tdee,
    target_calories,
    calories_consumed_today,
    remaining_calories,
)

@login_required
def dashboard(request):

    # Get logged-in user's profile
    profile = PersonalInfo.objects.filter(
        user=request.user
    ).first()

    # If no profile exists, send user to create one
    if not profile:
        return redirect("personal_info")

    # Get all meals of the logged-in user
    meals = Meal.objects.filter(
    user=request.user
    ).order_by("-meal_date", "-created_at")
    
    
    today_meals = Meal.objects.filter(
    user=request.user,
    meal_date=date.today()
    ).order_by("-created_at")


    # Today's calories
    today_calories = sum(
    meal.calory for meal in today_meals
    )

    # Meal counts
    total_meals = meals.count()

    today_meal_count = today_meals.count()

    # Average calories today
    if today_meal_count > 0:
         average_today = round(
        today_calories / today_meal_count,
        2
       )
    else:
        average_today = 0
    

    # Total calories of all meals
    total_calories = sum(
        meal.calory for meal in meals
    )

    # Nutrition calculations
    bmr = round(calculate_bmr(profile), 2)
    tdee = round(calculate_tdee(profile), 2)
    target = round(target_calories(profile), 2)
    consumed = calories_consumed_today(request.user)
    remaining = round(remaining_calories(profile), 2)
    recent_meals = meals[:5]

    context = {
        "profile": profile,
        "meals": meals, 
        "recent_meals": recent_meals,

        "total_calories": total_calories,

        "today_calories": today_calories,

        "total_meals": total_meals,

        "today_meal_count": today_meal_count,

        "average_today": average_today,

        "bmr": bmr,
        "tdee": tdee,
        "target": target,
        "consumed": consumed,
        "remaining": remaining,
    }

    return render(
        request,
        "dashboard/home.html",
        context,
    )