from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name=models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%M/%d/')
    description=models.TextField()
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    is_mvp=models.BooleanField(default=False)
    hire_date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

# Create your models here.
