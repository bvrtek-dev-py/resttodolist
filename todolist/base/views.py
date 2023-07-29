from rest_framework import decorators
from rest_framework import permissions
from rest_framework import generics
from rest_framework import response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .serializers import UserSerializer, CategorySerializer, TaskSerializer
from .models import Category, Task
from .permissions import IsOwnerOrReadOnly


@decorators.api_view(["GET"])
def api_root(request, format=None):
    return response.Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "categories": reverse("category-list", request=request, format=format),
            "tasks": reverse("task-list", request=request, format=format),
        }
    )


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryDetail(generics.RetrieveUpdateAPIView):
    serializer_class = CategorySerializer
    lookup_field = "uuid"
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    lookup_field = "uuid"
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "uuid"
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
