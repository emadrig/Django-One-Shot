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


def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("todo_list_list")
        else:
            form = TodoForm()

        context = {
            "form": form,
        }
        return render(request, "todo/create.html", context)
