from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    misc = models.TextField()
    recipe_type = models.CharField(max_length=100)
    source = models.CharField(max_length=100)

    class Meta:
        ordering = ["title"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["author"]),
            models.Index(fields=["recipe_type"]),
            models.Index(fields=["source"]),
        ]
