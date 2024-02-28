from django.db import models
from django.urls import reverse


class Item(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    name = models.CharField(max_length=30,
                            blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5,
                                decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id])
