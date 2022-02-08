from django.db import models
from django.core.validators import FileExtensionValidator

class MemberModel(models.Model):
    firstname = models.CharField(max_length=30)
    lastname =  models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=1)
    avatar = models.ImageField(upload_to='avatars/', validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    password = models.CharField(max_length=30)

class LikeModel(models.Model):
    sender = models.ForeignKey(MemberModel, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(MemberModel, on_delete=models.CASCADE, related_name='reciever')
