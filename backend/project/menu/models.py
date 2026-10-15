from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.TextField(blank = True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'menu_images', blank = True, null=True)
    is_available = models.BooleanField()
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.price}'