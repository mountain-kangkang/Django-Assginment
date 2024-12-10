from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from todo.models import Todo

@login_required()
def todo_list(request):
    todos = Todo.objects.filter(author=request.user)

    q = request.GET.get('q')
    if q:
        todos = todos.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q)
        )

    context = {'todos':todos}
    return render(request, 'todo_list.html', context)

def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {'todo':todo}
    return render(request, 'todo_info.html', context)
