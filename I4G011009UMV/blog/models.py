from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField
    author = models.ForeignKey('Curent user model', models.get_user_model)
    created_date = models.DateTimeField('date created')
    published_date = models.DateTimeField('date published')