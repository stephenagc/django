from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="Sem descrição disponível.")
    category = models.CharField(max_length=100)
    release_year = models.IntegerField()
    image = models.ImageField(upload_to='game_images/', blank=True, null=True)

    def __str__(self):
        return self.title
