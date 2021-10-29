from django.utils import timezone
from django.test import TestCase
from todolist import views
from todolist.models import Todo
from django.test import Client
import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase


class TodoTestViewCase(TestCase):

    def setUp(self):
        self.now = timezone.now()
        self.first_detail = 'firstdetail'
        self.csrf_client = Client(enforce_csrf_checks=False)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def test_view_url_exists_at_desired_location(self):
        request = self.factory.post('/loadtodos')
        # request.user = self.user
        request.user = AnonymousUser()
        response = views.loadtodos(request)
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        request = self.factory.get('')
        # request.user = self.user
        request.user = AnonymousUser()
        response = views.index(request)
        self.assertEqual(response.status_code, 302)

    def test_loadtodos_view(self):
        Todo.objects.create(title="Titre1", details="details1", state="RUN", state_order=0, created=self.now)
        Todo.objects.create(title="Titre2", details="details2", state="DONE", state_order=1)
        Todo.objects.create(title="Titre3", details="details3", state="INTER", state_order=2)
        Todo.objects.create(title="Titre4", details="", state="RUN", state_order=0)

        request = self.factory.post('/loadtodos')
        # request.user = self.user
        request.user = AnonymousUser()
        response = views.loadtodos(request)
        self.assertEqual(response.status_code, 200)

    # def test_new_todo(self):
    #     data = {"details": "azeaze"}
    #     request = self.factory.post('/addtodo/', data)
    #     # request.user = self.user
    #     request.user = AnonymousUser()
    #     response = views.addTodo(request)
    #     self.assertEqual(response.status_code, 200)
