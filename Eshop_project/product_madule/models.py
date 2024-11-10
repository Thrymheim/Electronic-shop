from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class product(models.Model):
    title = models.CharField(max_length=300) #charfield is for small amount of text unlile text field
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False) #if true user can see the product
    slug = models.SlugField(default='', null=False, db_index=True) #we use db_index for feilds we make lots of query on it cus makes query better

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # Call the save method of the superclass (models.Model) to actually save the object to the database.
        # This is crucial because it invokes all the necessary database operations.
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.price})'
