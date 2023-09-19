from mywebsite_api.recipes.models import Recipe
from .serializers import RecipeSerializer
from mywebsite_api.core.filters import (
    CamelCaseDjangoFilterBackend,
    CamelCaseOrderingFilter,
)
from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.mixins import NestedViewSetMixin


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (
        filters.SearchFilter,
        CamelCaseOrderingFilter,
        CamelCaseDjangoFilterBackend,
    )
    filterset_fields = {
        "title": ["icontains", "istartswith", "iendswith", "iexact"],
        "author": ["icontains", "istartswith", "iendswith", "iexact"],
        "recipe_type": ["icontains", "istartswith", "iendswith", "iexact"],
        "source": ["icontains", "istartswith", "iendswith", "iexact"],
    }

    search_fields = ["title", "author", "recipe_type", "source"]
