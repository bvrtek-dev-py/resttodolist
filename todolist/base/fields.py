# File for custom serializer fields

from rest_framework import serializers
from .models import Category


class CategoryHyperLinkedRelatedField(serializers.HyperlinkedRelatedField):
    def get_queryset(self):
        """
        Returns categories that are connected to specific user.
        """
        request = self.context["request"]
        return Category.objects.filter(user=request.user)
