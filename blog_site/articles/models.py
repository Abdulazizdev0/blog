from django.db import models

class Maqola(models.Model):

    WORLD = 'world'
    LOCAL = 'local'
    SPORT = 'sport'

    tag = (
        ('world', WORLD),
        ('local', LOCAL),
        ('sport', SPORT)

    )

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,null=True,blank=True)
    tag = models.CharField(max_length=10,choices=tag)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}  ---  {self.title}'
