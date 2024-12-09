from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todo_list'
