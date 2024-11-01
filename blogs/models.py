from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#category models
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  # to change name that displayed in admin models
    class Meta:
        verbose_name_plural ='Categories'
    
    def __str__(self):
        return self.category_name
#models blogs
STATUS_CHOICE = (
    ('draft','Draft'),
    ('published','Published')
)

class Blogs(models.Model):
    title= models.CharField(max_length=100, unique=True)
    #is the part of urls that identity particural page on website
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to= 'uploads/%y/%m/%d')
    short_description = models.TextField(max_length=2000)
    blog_body = models.TextField(max_length=10000)
    status = models.CharField(max_length=100 ,choices= STATUS_CHOICE, default='draft')
    is_feacherd =  models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

     # to change name that displayed in admin models
    class Meta:
        verbose_name_plural ='Blogs'

    def __str__(self):
        return self.title