from django.db import models

class product(models.Model):
    title = models.CharField(max_length=300) #charfield is for small amount of text unlile text field
    price = models.IntegerField()
