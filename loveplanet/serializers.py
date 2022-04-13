from rest_framework import serializers
from .models import MemberModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberModel
        fields = ('firstname', 'lastname', 'email', 'gender', 'avatar', 'password')

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=256)
    password = serializers.CharField(max_length=256)
