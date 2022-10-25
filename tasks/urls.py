from django.urls import path
from tasks.views import (
    show_my_tasks,
)

urlpatterns = [
    path("mine/", show_my_tasks, name="show_my_tasks"),
]
