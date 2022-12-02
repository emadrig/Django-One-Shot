from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList
from todos.forms import TodoForm

# Create your views here.


def todo_list_list(request):
    todo_list_list = TodoList.objects.all()
    context = {"todo_list_list": todo_list_list}
    return render(request, "todos/todo_list.html", context)


def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {"todo_list_detail": todo_list}
    return render(request, "todos/todo_detail.html", context)


def todo_list_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            list = form.save()

            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoForm()

    context = {
        "form": form,
    }
    return render(request, "todos/create.html", context)


def todo_list_update(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo_list)
        if form.is_valid():
            list = form.save()

            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoForm(instance=todo_list)

    context = {
        "todo_object": todo_list,
        "form": form,
    }
    return render(request, "todos/edit.html", context)


def todo_list_delete(request, id):
    todo_list = TodoList.objects.get(id=id)
    if request.method == "POST":
        todo_list.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")
