from django.shortcuts import render, get_object_or_404
from todo.models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    context = {'todos':todos}
    return render(request, 'todo_list.html', context)

def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {'todo':todo}
    return render(request, 'todo_info.html', context)
