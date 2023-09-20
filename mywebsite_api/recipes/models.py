from django.db import models
from mywebsite_api.core.model_abstracts import Model

class Recipe(Model):
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

    def __str__(self) -> str:
        return f"{self.title}"
