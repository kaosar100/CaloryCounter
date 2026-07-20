from django.urls import path
from .views import personal_info, delete_profile
from .api_views import PersonalInfoAPIView

urlpatterns = [
    path('profile/', personal_info, name='personal_info'),
    path('delete_profile/', delete_profile, name="delete_profile"),
    
    #api views
    path('api/profile/', PersonalInfoAPIView.as_view(), name='api_profile'),
    
]