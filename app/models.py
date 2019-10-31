from django.db import models

# Create your models here.
class Model_img(models.Model):
    img=models.ImageField(upload_to='images/')
    