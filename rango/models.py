from django.db import models

# Create your models here.
#exercise 5.3

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    #line below added in excercise at end of 5
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    #below class meta edited in ex 5.6
    class Meta:
        verbose_name_plural = 'Categories'

    
    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
