from django.test import TestCase
from .models import Task
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .forms import Taskform
from django.urls import reverse
from rest_framework import status

class TaskModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='blest905',
            email='blest905@gmail.com',
            password='33458106'
        )
    

    def test_create_task(self):
        task = Task.objects.create(
            title='Тестовая задача',
            description='Тестовое описание',
            completed=False,
            user=self.user
        )

        self.assertEqual(task.title, 'Тестовая задача')    
        self.assertEqual(task.description, 'Тестовое описание')  
        self.assertEqual(task.completed, False)  
        self.assertEqual(task.user, self.user)  

    def task_str_method_test(self):
        task = Task.objects.create(
            title='Задача',
            user=self.user
        )

        self.assertEqual(str(task), 'Задача')

class TaskFormTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='blest905',
            email='blest905@gmail.com',
            password='33458106'
        )

    def test_valid_form(self):
        form_data = {
            'title':'Задача',
            'description':'Описание'
        }
        form = Taskform(data=form_data)
        self.assertTrue(form.is_valid())

        def test_invalid_form(self):
            form_data = {
            'description': 'Описание без заголовка'
            }
            form = TaskForm(data=form_data)
            self.assertFalse(form.is_valid())
            self.assertIn('title', form.errors)
            

class TaskViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='blest905',
            email='blest905@gmail.com',
            password='33458106'
        )

        self.task1 = Task.objects.create(
            title='Тестовая задача 1',
            description='Тестовое описание 1',
            user=self.user
        )

        self.task2 = Task.objects.create(
            title='Тестовая задача 2',
            description='Тестовое описание 2',
            user=self.user
        )

    def test_notloginuser_onlist(self):
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/list/')

    def test_login_user(self):
        self.client.login(username='blest905', password='33458106')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовая задача 1')
        self.assertContains(response, 'Тестовая задача 2')
        self.assertTemplateUsed(response, 'taskapp/task_list.html')

class TaskApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='blest905', email='blest905@gmail.com', password='33458106')
        self.task = Task.objects.create(title='Название API 1', description='Описание API 1', user=self.user)
        self.client.login(username='blest905', password='33458106')

    def test_create_task_api(self):
        url = '/api/tasks/'
        data = {'title': 'Название api 2', 'description': 'Описание api 2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_task_list(self):
        url = '/api/tasks/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertEqual(Task.objects.count(), 1)
    
    def test_get_single_task(self):
        url = f'/api/tasks/{self.task.id}/'
        response = self.client.get(url)
        self.assertEqual(response.data['title'], 'Название API 1')

    def test_update_task(self):
        url = f'/api/tasks/{self.task.id}/'
        data = {'title': f'Обновлённое название задачи {self.task.id}', 'description': 'Новое описание'}
        response = self.client.put(url, data, format='json')
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.task.title, f'Обновлённое название задачи {self.task.id}')

    def test_delete_task(self):
        url = f'/api/tasks/{self.task.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_notd_defined_user(self):
        self.client.logout()
        url = f'/api/tasks/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


        response = self.client.post(reverse('account_signup'), {
            'email': 'blest905@gmail.com',
            'password1': '13371324nv',
            'password2': '13371324nv'
        })