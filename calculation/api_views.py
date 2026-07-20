from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import PersonalInfo
from .utils import calculate_bmr, calculate_tdee, target_calories, calories_consumed_today, remaining_calories


class CalculationAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            profile = PersonalInfo.objects.get(user=request.user)
        except PersonalInfo.DoesNotExist:
            return Response({"message":"profile not found"}, status=404)
        
        data = {
            "username": request.user.username,
            "bmr": round(calculate_bmr(profile), 2),
            "tdee": round(calculate_tdee(profile), 2),
            "target_calories": round(target_calories(profile), 2),
            "consumed_today": calories_consumed_today(request.user),
            "remaining_calories": round(remaining_calories(profile), 2),
        }
        
        return Response(data)