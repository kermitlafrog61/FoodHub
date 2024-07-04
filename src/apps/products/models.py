from django.db import models


class Product(models.Model):
    TYPE_CHOICES = [
        ('salad', 'Salad'),
        ('soup', 'Soup'),
        # TODO: ask Toktosun about other types
    ]

    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)
    popularity = models.PositiveIntegerField(default=0)
    novelty = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
