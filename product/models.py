from django.db import models

PRODUCT_CHOICES = (
    ("1","first"),
    ("2","second"),
    ("3","third"),
    ("4","fourth")
)

class ProductsModel(models.Model):
    name = models.CharField(max_length=255)
    types = models.CharField(max_length=4,choices=PRODUCT_CHOICES,default=1)
    summary = models.CharField(max_length=255)
    body = models.TextField()
    photo = models.ImageField()


    def __str__(self) :
        return self.name
    

    class Meta:
        db_table = 'Products'

    

