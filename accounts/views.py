from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AccountSerializer



class AccountAPIView(APIView):

    """
    Creating the newuser
    """

    def post(self, request,format=None):
        """
        create a new user
        """
        inputs = request.data
        print(inputs)
        serializer = AccountSerializer(data=inputs)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
