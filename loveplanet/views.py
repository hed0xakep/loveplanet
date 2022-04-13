from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer
from rest_framework import generics
from rest_framework import status
from .models import MemberModel
from django.core.mail import send_mail
from PIL import Image
from django.conf import settings

HOST_EMAIL = settings.EMAIL_HOST_USER



class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data['email']
        #if MemberModel.objects.filter(email=email).exists():
            #return Response({'User with this email already exists':f'{email}'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        print(serializer.validated_data['avatar'])
        return Response(status=status.HTTP_201_CREATED)

class LikeView(APIView):
    def post(self, request, id):
        serializer = LoginSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password=serializer.validated_data['password']
        if MemberModel.objects.filter(email=email, password=password).exists():
                    if MemberModel.objects.filter(id=id).exists():
                        sender = MemberModel.objects.get(email=email)
                        reciever = MemberModel.objects.get(id=id)

                        if LikeModel.objects.filter(sender=reciever, reciever=sender):

                            send_mail('Взаимная симпатия!', f'Вы понравились \
                            пользователю {sender.firstname} {sender.lastname}! \
                            Почта участника: {sender.email}', HOST_EMAIL, (reciever.email,))

                            send_mail('Взаимная симпатия!', f'Вы понравились \
                            пользователю {reciever.firstname} {reciever.lastname}! \
                            Почта участника: {reciever.email}', HOST_EMAIL, (sender.email,))
                            return Response(status=status.HTTP_200_OK)

                        LikeModel.objects.create(sender=sender, reciever=reciever)
                        return Response(status=status.HTTP_200_OK)

                    return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
