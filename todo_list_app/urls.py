from django.urls import path

from todo_list_app.views import (
    TaskListView,
    complete_undo_task,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("<int:pk>", complete_undo_task, name="complete_undo_task"),
    path("add/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag_delete")
]


app_name = "todo_list"
