from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework import status
from .models import MemberModel

class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data['email']
        if MemberModel.objects.filter(email=email).exists():
            return Response({'User with this email already exists':f'{email}'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
