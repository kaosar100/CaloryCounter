from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import PersonalInfo
from .serializers import PersonalInfoSerializer

class PersonalInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    #GET api profile    
    def get(self, request):
        try:
            profile = PersonalInfo.objects.get(user = request.user)
        
        except PersonalInfo.DoesNotExist:
            return Response(
                {
                    "message":"Profile not found"
                },
                status=status.HTTP_404_NOT_FOUND,
            ) 
        serializer = PersonalInfoSerializer(profile)
        return Response(serializer.data)
    
    #POST api profile
    def post(self, request):
        if PersonalInfo.objects.filter(user=request.user).exists():
            return Response(
                {
                    'message':"Profile already exists"
                },
                status = status.HTTP_400_BAD_REQUEST,
            )
        
        serializer = PersonalInfoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(data=request.data)
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # PUT /api/profile/
    def put(self, request):

        try:
            profile = PersonalInfo.objects.get(user=request.user)

        except PersonalInfo.DoesNotExist:

            return Response(
                {
                    "message": "Profile not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PersonalInfoSerializer(
            profile,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    # DELETE /api/profile/
    def delete(self, request):

        try:
            profile = PersonalInfo.objects.get(user=request.user)

        except PersonalInfo.DoesNotExist:

            return Response(
                {
                    "message": "Profile not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        profile.delete()

        return Response(
            {
                "message": "Profile deleted successfully."
            },
            status=status.HTTP_204_NO_CONTENT
        )
        
        
        
        
        
    
       