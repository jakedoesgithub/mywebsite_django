from django.db import transaction
from rest_framework import serializers
from mywebsite_api.recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "id",
            "title",
            "author",
            "ingredients",
            "instructions",
            "misc",
            "recipe_type",
            "source",
        )

    @transaction.atomic
    def create(self, validated_data):
        instance = Recipe()
        # Set regular attrs
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        # Set regular attrs
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        self._create_or_update_address(instance)

        instance.save()
        return instance