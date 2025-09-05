from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def dashboard(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'todo_main/dashboard.html', {'todos': todos})


def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')

        if title:
            Todo.objects.create(
                title=title,
                description=description
            )
    return redirect('dashboard')


def delete_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()

    return redirect('dashboard')


def toggle_todo(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=todo_id)
        todo.completed = not todo.completed
        todo.save()

    return redirect('dashboard')
