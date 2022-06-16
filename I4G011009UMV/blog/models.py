from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField
    User = get_user_model()
    author = models.ForeignKey( User, on_delete=models.CASCADE,)
    created_date = models.DateTimeField('date created')
    published_date = models.DateTimeField('date published')