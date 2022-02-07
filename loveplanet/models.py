from django.db import models
from django.core.validators import FileExtensionValidator

class User(models.Model):
    GENDERS = (
        ('m', 'Man'),
        ('w', 'Woman')
    )
    firstname = models.CharField(max_length=30)
    lastname =  models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    avatar = models.ImageField(upload_to='avatars/', validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    password = models.CharField(max_length=30)
