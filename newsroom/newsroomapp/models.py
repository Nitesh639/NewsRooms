from django.db import models

class news_details(models.Model):
    title = models.TextField(max_length=1000,null=True)
    img_url = models.TextField(max_length=1000,null=True)
    date = models.DateTimeField(null=True)
    source = models.TextField(max_length=200,null=True)
