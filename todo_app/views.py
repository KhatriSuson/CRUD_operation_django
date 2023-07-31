from django.shortcuts import render, HttpResponseRedirect
from todo_app.models import Todo

# Create your views here.


def todo_create(request):
    if request.method == "GET":
        return render(request, "bootstrap/todo_create.html")
    else:
        title = request.POST["title"]
        Todo.objects.create(title=title)
        return HttpResponseRedirect("/")


def todo_list(request):
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, "bootstrap/todo_list.html", context)


def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "GET":
        return render(
            request,
            "bootstrap/todo_update.html",
            {"todo": todo},
        )

    else:
        todo.title = request.POST["title"]
        todo.save()
        return HttpResponseRedirect("/")


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect("/")
