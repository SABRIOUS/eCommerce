from django.db import models
from django.db.models import Q

import random
import os
from .utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.urls import reverse

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
class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True,active=True)
    def active(self):
        return self.filter(active=True)

    def search(self,query):
        lookups = Q(title__icontains=query)| Q(description__icontains=query)
        return self.filter(lookups).distinct()

class ProductManger(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)
    def all(self):
        return self.get_queryset().active()
    def features(self):
        return self.get_queryset().featured()

    def get_by_id(self,id):
        #Product.objects == self.queryset() in shell
        qs =  self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None

    def search(self,query):
        lookups = (Q(title__icontains=query)|
                  Q(description__icontains=query)|
                  Q(price__icontains=query)|
                  Q(tag__title__icontains=query))


        return self.filter(lookups).distinct()

class Product(models.Model):
    title = models.CharField(max_length=120)
    # unique slug means there will be one slug for each product with no repeat
    slug = models.SlugField(blank=True,unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=20,default=39.99)
    # blank means not required & null means it can be empty
    image = models.ImageField(upload_to=upload_iamge_path,null = True,blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = ProductManger()

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={"slug":self.slug})
    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.title

def product_pre_save_reveiver(sender, instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_reveiver,sender=Product)
