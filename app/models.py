from django.db import models

# Create your models here.


class upload_project(models.Model):
    pname = models.CharField(max_length=100)
    pdesc = models.TextField()
    url = models.URLField()
    technologies = models.TextField()
    profile_picture = models.ImageField(upload_to='')
    upload_date=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.pname