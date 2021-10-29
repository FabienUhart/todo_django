from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader
from todolist import models
import json
import logging

TEMPLATES = {
    'todos': 'todos.html',
}

logger = logging.getLogger(__name__)


def index(request):
    """Index."""
    return redirect('/static/home/index.html')


@ensure_csrf_cookie
@csrf_exempt
def loadtodos(request):
    todos_run = models.Todo.objects.all().order_by('state_order','-created')
    template = loader.get_template(TEMPLATES['todos'])
    listTodoHtml = template.render({
        'todos': todos_run,
    })
    logger.info('loadtodos')
    return HttpResponse(listTodoHtml)


@ensure_csrf_cookie
@csrf_exempt
def addTodo(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode("utf-8"))
    else:
        return JsonResponse(
            {
                'error': 'problem POST addTodo'
            }, status=404)
    logger.info('addNewTodo')
    logger.info(received_json_data['details'])
    todo = models.Todo(title=received_json_data['details'], state='RUN', state_order=0)
    todo.save()
    return JsonResponse(
        {
            'id': todo.id,
            'title': todo.title
        }, status=200)
