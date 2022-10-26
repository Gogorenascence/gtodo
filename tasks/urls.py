from django.urls import path
from tasks.views import (
    show_my_tasks,
    create_task,
)

urlpatterns = [
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("create/", create_task, name="create_task"),
]
