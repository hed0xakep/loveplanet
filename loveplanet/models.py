from django.db import models
from django.core.validators import FileExtensionValidator
from PIL import Image, ImageDraw, ImageFont

class MemberModel(models.Model):
    firstname = models.CharField(max_length=30)
    lastname =  models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=1)
    avatar = models.ImageField(upload_to='avatars/', validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    password = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super(MemberModel, self).save(*args, **kwargs)
        image = Image.open(self.avatar.path)
        width, height = image.size
        draw = ImageDraw.Draw(image)
        text = "loveplanet.com"
        font = ImageFont.truetype('arial.ttf', 50)
        textwidth, textheight = draw.textsize(text, font)
        margin = 5
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x, y), text, font=font)
        image.save(self.avatar.path)

class LikeModel(models.Model):
    sender = models.ForeignKey(MemberModel, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(MemberModel, on_delete=models.CASCADE, related_name='reciever')
