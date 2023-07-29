from rest_framework import serializers
from .models import Category, Task
from . import fields
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    categories = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="category-detail", lookup_field="uuid"
    )
    tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "categories",
            "tasks",
        )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="category-detail", lookup_field="uuid"
    )
    user = serializers.HyperlinkedRelatedField(
        view_name="user-detail",
        read_only=True,
    )
    tasks = serializers.HyperlinkedRelatedField(
        view_name="task-detail", many=True, read_only=True, lookup_field="uuid"
    )

    class Meta:
        model = Category
        fields = ("url", "user", "name", "tasks")


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField("user-detail", read_only=True)
    url = serializers.HyperlinkedIdentityField("task-detail", lookup_field="uuid")
    category = fields.CategoryHyperLinkedRelatedField(
        "category-detail", lookup_field="uuid"
    )

    class Meta:
        model = Task
        fields = (
            "url",
            "user",
            "category",
            "name",
            "short_description",
            "is_done",
            "started_at",
            "term",
            "time_left",
            "task_time",
        )
