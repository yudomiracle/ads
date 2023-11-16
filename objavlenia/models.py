from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()

class Advertisment(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    info = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

class Comment(models.Model):
    advertisment = models.ForeignKey(Advertisment, on_delete=models.CASCADE)
    text = models.TextField()
    posted_time = models.DateField(auto_now_add=True)
