from .serializers import MealSerializer
from .models import Meal

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class MealListCreateAPIViews(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        meal = Meal.objects.filter(
            user= request.user,
            ).order_by("-meal_date", "-created_at")
        
        serializer = MealSerializer(
            meal, many= True,
        )
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save(user=request.user)
           
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class MealDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, request, id):

        try:
            return Meal.objects.get(
                id=id,
                user=request.user
            )

        except Meal.DoesNotExist:
            return None

    # GET /api/meals/<id>/
    def get(self, request, id):

        meal = self.get_object(request, id)

        if meal is None:
            return Response(
                {"message": "Meal not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MealSerializer(meal)

        return Response(serializer.data)

    # PUT /api/meals/<id>/
    def put(self, request, id):

        meal = self.get_object(request, id)

        if meal is None:
            return Response(
                {"message": "Meal not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MealSerializer(
            meal,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE /api/meals/<id>/
    def delete(self, request, id):

        meal = self.get_object(request, id)

        if meal is None:
            return Response(
                {"message": "Meal not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        meal.delete()

        return Response(
            {"message": "Meal deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )