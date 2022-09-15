from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'brand'


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    detail = models.TextField()
    brand = models.ForeignKey(Brand, related_name="product_brand",on_delete=models.CASCADE)                
    category = models.ForeignKey(Category, related_name="product_category",on_delete=models.CASCADE)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product/',default= "product/default.png")
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'products'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url