from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Meal
from.forms import MealForm
# Create your views here.
@login_required
def meal_list(request):
    meal = Meal.objects.filter(user=request.user).order_by('-meal_date', '-created_at')
    
    context = {
        'meal': meal
    }
    
    return render(request, 'meals/meal_list.html', context)

@login_required
def meal_create(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('meal_list')
    else:
        form = MealForm()
    return render(request, 'meals/meal_form.html', {'form':form})

@login_required
def meal_details(request, id):
    meal = get_object_or_404(Meal, id = id, user=request.user)
    return render(request, 'meals/meal_detail.html', {'meal':meal})

@login_required
def update_meal(request, id):
    meal = get_object_or_404(Meal, user=request.user, id=id)
    if request.method == "POST":
        form = MealForm(request.POST, instance=meal)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('meal_list')
    else:
        form = MealForm(instance=meal)
    return render(request, 'meals/meal_form.html', {'form':form})

@login_required
def delete_meal(request, id):
    meal = get_object_or_404(Meal, user = request.user, id = id)
   
    meal.delete()
    
    
    return redirect('meal_list')
    
    
    
    