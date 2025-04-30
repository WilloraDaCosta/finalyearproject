from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=50)
    bf = models.IntegerField() #breakfast
    lu = models.IntegerField() #lunch
    di = models.IntegerField() #dinner
    cal = models.IntegerField() #calories
    fat = models.IntegerField() 
    pro = models.IntegerField()
    sug = models.IntegerField()
    imagepath= models.CharField(default="",max_length=100)

    def __str__(self):
        return self.name
