from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.api_root, name="root"),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("user/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("categories/", views.CategoryList.as_view(), name="category-list"),
    path(
        "category/<str:uuid>/", views.CategoryDetail.as_view(), name="category-detail"
    ),
    path("tasks/", views.TaskList.as_view(), name="task-list"),
    path("task/<str:uuid>/", views.TaskDetail.as_view(), name="task-detail"),
]


urlpatterns += [path("auth-api/", include("rest_framework.urls"))]
