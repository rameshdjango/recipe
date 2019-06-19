from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Recipie_creater(models.Model):
    user_name = models.OneToOneField(User,on_delete =models.CASCADE)
    name = models.CharField(max_length=50)

class Recipie (models.Model):
    creater_name = models.ForeignKey(Recipie_creater,on_delete = models.CASCADE)
    recipie_name = models.CharField(max_length = 50)
    ingredients = models.CharField(max_length =250)
    process = models.TextField()
    file_upload = models.FileField(upload_to='media/uploads/%Y/%m/%d/', null=True, blank=True)
