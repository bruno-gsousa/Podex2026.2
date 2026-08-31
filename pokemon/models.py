from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    types = models.CharField(max_length=200)
    abilities = models.CharField(max_length=200)
    image = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
     
