from django.utils import timezone
from django.test import TestCase
from todolist.models import Todo


class TodoTestCase(TestCase):
    def setUp(self):
        self.now = timezone.now()
        Todo.objects.create(title="Titre1", details="details1", state="RUN", state_order=0, created=self.now)
        Todo.objects.create(title="Titre2", details="details2", state="DONE", state_order=1)
        Todo.objects.create(title="Titre3", details="details3", state="INTER", state_order=2)
        Todo.objects.create(title="Titre4", details="", state="RUN", state_order=0)

    def test_todo(self):
        firstTitle = Todo.objects.get(title="Titre1")
        secondTitle = Todo.objects.get(title="Titre2")
        thirdTitle = Todo.objects.get(title="Titre3")
        fourthTitle = Todo.objects.get(title="Titre4")
        self.assertEqual(getattr(firstTitle, 'created'), self.now)
        self.assertEqual(getattr(secondTitle, 'details'), 'details2')
        self.assertEqual(getattr(thirdTitle, 'state'), 'INTER')
        self.assertEqual(getattr(fourthTitle, 'state_order'), 0)
