from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AccountSerializer



class AccountAPIView(APIView):

    """
    Creating the newuser
    """
    
    def post(self, request):
        """
        create a new user
        """
        inputs = request.data
        
        serializer = AccountSerializer(data=inputs)

        print(serializer.initial_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
