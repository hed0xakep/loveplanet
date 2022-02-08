from rest_framework import serializers
from .models import MemberModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberModel
        fields = ('firstname', 'lastname', 'email', 'gender', 'avatar', 'password')
