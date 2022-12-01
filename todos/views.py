from django.shortcuts import render
from .models import TodoList

# Create your views here.


def todo_list_list(request):
    todo_list_list = TodoList.objects.all()
    context = {"todo_list_list": todo_list_list}
    return render(request, "todos/todo_list.html", context)
