from django import forms
from todo_list_app.models import Tasks, Tags


class TasksForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Tasks
        fields = "title","deadline", "tags"
