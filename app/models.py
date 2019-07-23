from django.db import models

# Create your models here.
class Delivery(models.Model):
    name= models.TextField(primary_key = True)
    housetype = models.TextField()
    kind_of_news = models.TextField()
    images = models.TextField(null=True)
    etc = models.TextField(null=True)
    def __str__(self):
        return self.name
