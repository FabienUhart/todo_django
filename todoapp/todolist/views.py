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
    'todo': 'todo.html',
}

logger = logging.getLogger(__name__)


def index(request):
    """Index."""
    return redirect('/static/home/index.html')


@ensure_csrf_cookie
@csrf_exempt
def loadTodos(request):
    todos_run = models.Todo.objects.all().order_by('state_order', '-created')
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


@ensure_csrf_cookie
@csrf_exempt
def getTodo(request, id):
    if request.method == 'GET':
        logger.info(id)
        try:
            todo = models.Todo.objects.get(id=int(id))
            template = loader.get_template(TEMPLATES['todo'])
            getTodoHtml = template.render({
                'todo': todo,
            })
            logger.info('getTodo')
            return HttpResponse(getTodoHtml)
        except models.Todo.DoesNotExist:
            return redirect('/static/home/index.html')
    else:
        return JsonResponse(
            {
                'error': 'problem POST getTodo'
            }, status=404)

    # todo = models.Todo.objects.get(id=received_json_data['id'])
    return JsonResponse({'id': id}, status=200)


@ensure_csrf_cookie
@csrf_exempt
def updateTodo(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode("utf-8"))
        todo = models.Todo.objects.get(id=received_json_data['id'])
        for key in received_json_data.keys(): setattr(todo, key, received_json_data[key])
        todo.save()
        return JsonResponse(received_json_data, status=200)
    else:
        return JsonResponse(
            {'error': 'problem POST updateTodo'}, status=404)
