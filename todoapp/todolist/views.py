from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader
from todolist import models


TEMPLATES = {
    'todos': 'todos.html',
}


def index(request):
    """Index."""
    return redirect('/static/home/index.html')


@ensure_csrf_cookie
@csrf_exempt
def loadtodos(request):
    todos_run = models.Todo.objects.all().order_by('-created').order_by('state_order')
    template = loader.get_template(TEMPLATES['todos'])
    listTodoHtml = template.render({
        'todos': todos_run,
    })
    return HttpResponse(listTodoHtml)
