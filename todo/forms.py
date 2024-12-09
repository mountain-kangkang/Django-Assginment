from django import forms

from todo.models import Todo

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'is_completed')