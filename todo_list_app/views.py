from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list_app.forms import TasksForm
from todo_list_app.models import Tasks, Tags


class TaskListView(generic.ListView):
    model = Tasks
    template_name = "to_do_list/index.html"
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    form_class = TasksForm
    success_url = reverse_lazy("todo_list:index")
    template_name = "to_do_list/task_create.html"


class TaskUpdateView(generic.UpdateView):
    model = Tasks
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")
    template_name = "to_do_list/task_create.html"


class TaskDeleteView(generic.DeleteView):
    model = Tasks
    success_url = reverse_lazy("todo_list:index")
    template_name = "to_do_list/task_delete.html"



class TagListView(generic.ListView):
    model = Tags
    template_name = "to_do_list/tags_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag_list")
    template_name = "to_do_list/tag_create.html"


class TagUpdateView(generic.UpdateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag_list")
    template_name = "to_do_list/tag_create.html"


class TagDeleteView(generic.DeleteView):
    model = Tags
    success_url = reverse_lazy("todo_list:tag_list")
    template_name = "to_do_list/tag_confirm_delete.html"


def complete_undo_task(request, pk):
    task = Tasks.objects.get(id=pk)
    created_at = task.created_at
    task.is_complete = not task.is_complete
    task.created_at = created_at
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo_list:index"))
