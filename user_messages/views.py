"""
The view class for user_messages
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_messages.serializers import UserMessageSerializer

class UserMessageAPIView(APIView):
    """
    creating the new message of the user
    """
    def post(self, request):
        """
        the method that takes the request post and send data to the  
        database
        """
        inputs = request.data
        serializer = UserMessageSerializer(data=inputs)
        
        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

