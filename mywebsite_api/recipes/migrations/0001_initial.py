# Generated by Django 4.1.2 on 2023-09-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("ingredients", models.TextField()),
                ("instructions", models.TextField()),
                ("misc", models.TextField()),
                ("recipe_type", models.CharField(max_length=100)),
                ("source", models.CharField(max_length=100)),
            ],
            options={
                "ordering": ["title"],
            },
        ),
        migrations.AddIndex(
            model_name="recipe",
            index=models.Index(fields=["title"], name="recipes_rec_title_9ebae8_idx"),
        ),
        migrations.AddIndex(
            model_name="recipe",
            index=models.Index(fields=["author"], name="recipes_rec_author_8ede29_idx"),
        ),
        migrations.AddIndex(
            model_name="recipe",
            index=models.Index(
                fields=["recipe_type"], name="recipes_rec_recipe__e6ccd4_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="recipe",
            index=models.Index(fields=["source"], name="recipes_rec_source_b6db08_idx"),
        ),
    ]