from django.db import models


class Article(models.Model):
    text = models.TextField(default='text of article')
