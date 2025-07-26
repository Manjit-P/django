from django.test import TestCase
from django.utils import timezone
from .models import Task

class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(
            name = 'shiiit',
            description = 'nah',
            category = 'D',
            created_on = "2025-7-15",
            due = "2025-7-15",
            completed = False,
            slug = 'shiiit' ,
        )

        self.assertEqual(task.name,'shiiit')
        self.assertEqual(task.description,'nah')
        self.assertEqual(task.category,'D')
        self.assertEqual(task.created_on,"2025-7-15")
        self.assertEqual(task.due,"2025-7-15")
        self.assertEqual(task.slug,'shiiit')
        self.assertFalse(task.completed,False)

    def test_update_task(self):
        task = Task