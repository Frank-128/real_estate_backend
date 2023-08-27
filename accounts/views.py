from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountAPIView(APIView):

    """
    Creating the new user
    """

    def post(self, request):
        """
        create a new user
        """
        inputs = request.data

        serializer = AccountSerializer(data=inputs)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request,format=None):
        all_data = Account.objects.all()
        serializer = AccountSerializer(all_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
