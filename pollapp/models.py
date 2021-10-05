from django.db import models

# Create your models here.

class Polls(models.Model):
    question=models.TextField(max_length=200)
    option_a=models.CharField(max_length=50)
    option_b = models.CharField(max_length=50)
    option_c = models.CharField(max_length=50)
    a_count=models.IntegerField(default=0)
    b_count = models.IntegerField(default=0)
    c_count = models.IntegerField(default=0)
