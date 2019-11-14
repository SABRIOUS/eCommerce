from django.db import models
import random
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_iamge_path(instance, filename):
    new_filename = random.randint(1,39152145101)
    name, ext = get_filename_ext(filename)
    final_filename = f"{new_filename}{ext}"
    return f"products/{new_filename}/{final_filename}"

# Create your models here.
class ProductManger(models.Manager):
    def get_by_id(self,id):
        #Product.objects == self.queryset() in shell
        qs =  self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None



class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=20,default=39.99)
    # blank means not required & null means it can be empty
    image = models.ImageField(upload_to=upload_iamge_path,null = True,blank=True)

    objects = ProductManger()

    def __str__(self):
        return self.title
