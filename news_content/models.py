from django.db import models


# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=150)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12, default="00:00")
    writer = models.CharField(max_length=50, null=True, blank=True)
    picname = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    act = models.IntegerField(default=0)

    def __str__(self):
        return self.name
