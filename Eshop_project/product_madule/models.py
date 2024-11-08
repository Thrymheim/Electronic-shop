from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class product(models.Model):
    title = models.CharField(max_length=300) #charfield is for small amount of text unlile text field
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False) #if true user can see the product

    def __str__(self):
        return f'{self.title} ({self.price})'