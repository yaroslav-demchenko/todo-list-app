from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Tasks(models.Model):
    title = models.CharField("Yor task", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_complete = models.BooleanField("Complete", default=False)
    tags = models.ManyToManyField(Tags, related_name="tasks")

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["is_complete", "created_at"]

    def __str__(self):
        return self.title
