from django.db import models

#ex 6.3
from django.template.defaultfilters import slugify

# Create your models here.
#exercise 5.3

class Category(models.Model):
    max_length = 128
    name = models.CharField(max_length = max_length, unique=True)
    #line below added in excercise at end of 5
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    
    #edited 6.3 twice
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    
    #below class meta edited in ex 5.6
    class Meta:
        verbose_name_plural = 'Categories'

    
    def __str__(self):
        return self.name

class Page(models.Model):
    max_length = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length= max_length)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
