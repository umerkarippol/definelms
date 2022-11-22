from django.db import models


class designation(models.Model):
    designation = models.CharField(max_length=200)
    def __str__(self):
        return self.name
        

