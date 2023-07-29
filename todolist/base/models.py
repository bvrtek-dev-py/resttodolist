from django.db import models
import datetime
from uuid import uuid4


class Category(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="categories"
    )
    uuid = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="tasks"
    )
    uuid = models.UUIDField(default=uuid4, editable=False)
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="tasks"
    )
    short_description = models.TextField(max_length=255, blank=True, null=True)
    is_done = models.BooleanField(default=False)
    started_at = models.DateField(default=datetime.date.today)
    term = models.DateField(default=datetime.date.today)

    @property
    def time_left(self):
        return self.term - datetime.date.today()

    @property
    def task_time(self):
        return self.term - self.started_at

    def __str__(self):
        return self.name
