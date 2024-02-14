from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from .views import signup, login, save_json

class SignupLoginJsonTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_signup_success(self):
        request = self.factory.post('/signup/', {'username': 'new_user', 'password': 'new_password'}, content_type="application/json")
        response = signup(request)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data['message'], 'registration succeeded')

    def test_signup_user_exist(self):
        request = self.factory.post('/signup/', {'username': self.username, 'password': self.password}, content_type="application/json")
        response = signup(request)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data, {'error': 'user exist'})

    def test_login_success(self):
        request = self.factory.post('/login/', {'username': self.username, 'password': self.password}, content_type="application/json")
        response = login(request)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data, {'message': 'login succeeded'})

    def test_login_wrong_credentials(self):
        request = self.factory.post('/login/', {'username': 'wrong_user', 'password': 'wrong_password'}, content_type="application/json")
        response = login(request)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data, {'error': 'wrong username or password'})

    def test_save_json_success(self):
        json_data = {'key': 'value'}
        request = self.factory.post('/save_json/', {'username': self.username, 'json_data': json.dumps(json_data)}, content_type="application/json")
        response = save_json(request)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data, {'message': 'JSON data saved successfully'})

    def test_save_json_user_not_found(self):
        json_data = {'key': 'value'}
        request = self.factory.post('/save_json/', {'username': 'non_existing_user', 'json_data': json.dumps(json_data)}, content_type="application/json")
        response = save_json(request)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data, {'error': 'User not found'})

    def test_save_json_wrong_method(self):
        request = self.factory.get('/save_json/')
        response = save_json(request)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data, {'error': 'Method must be POST'})
