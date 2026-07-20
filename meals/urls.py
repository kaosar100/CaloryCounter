from django.urls import path
from .views import meal_create, meal_details, meal_list, delete_meal, update_meal
from .api_views import MealListCreateAPIViews, MealDetailAPIView
urlpatterns = [
    path('', meal_list, name='meal_list'),
    path('create/', meal_create, name='meal_create'),
    path('d/<int:id>/', meal_details, name='meal_details'),
    path('edit/<int:id>/', update_meal, name='meal_update'),
    path('delete/<int:id>', delete_meal, name='meal_delete'),
    
    #api_views
    path("api/meals/", MealListCreateAPIViews.as_view(), name="api_meal_list",),

    path("api/meals/d/<int:id>/",MealDetailAPIView.as_view(),name="api_meal_detail",),
    
]
