from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["last_name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

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
