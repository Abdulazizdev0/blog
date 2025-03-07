from django.db import models

class Maqola(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
