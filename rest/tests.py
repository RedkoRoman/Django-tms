import json
import os

import django
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()


class AuthorViewSetTests(TestCase):

    def setUp(self):
        self.author_model = apps.get_model('rest', 'Author')
        self.book_model = apps.get_model('rest', 'Book')
        self.author_data_1 = {
            'first_name': 'Petr',
            'last_name': 'Petrov',
            'email': 'pp@gmail.com',
            'birth_date': '2000-01-01',
        }
        self.author_data_2 = {
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'email': 'ii@gmail.com',
            'birth_date': '2010-01-01',
        }
        self.author_1 = self.author_model.objects.create(**self.author_data_1)
        self.author_2 = self.author_model.objects.create(**self.author_data_2)

    def test_list_authors(self):
        response = self.client.get(path=reverse('authors-list'))
        authors = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(authors, list))

        self.assertEqual(len(authors), 2)

        self.assertEqual(authors[0]['id'], self.author_1.id)
        self.assertEqual(authors[0]['first_name'], self.author_1.first_name)
        self.assertEqual(authors[0]['last_name'], self.author_1.last_name)
        self.assertEqual(authors[0]['email'], self.author_1.email)
        self.assertEqual(authors[0]['birth_date'], self.author_1.birth_date)

        self.assertEqual(authors[1]['id'], self.author_2.id)
        self.assertEqual(authors[1]['first_name'], self.author_2.first_name)
        self.assertEqual(authors[1]['last_name'], self.author_2.last_name)
        self.assertEqual(authors[1]['email'], self.author_2.email)
        self.assertEqual(authors[1]['birth_date'], self.author_2.birth_date)

    def test_create_authors(self):
        author_data = {
            'first_name': 'Joe',
            'last_name': 'Ban',
            'email': 'jb@gmail.com',
            'birth_date': '2000-01-01',
        }
        response = self.client.post(reverse('authors-list'), author_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        author = self.author_model.objects.get(email=author_data['email'])

        self.assertEqual(author.id, response.data['id'])
        self.assertEqual(author.first_name, author_data['first_name'])
        self.assertEqual(author.last_name, author_data['last_name'])
        self.assertEqual(author.email, author_data['email'])
        self.assertEqual(str(author.birth_date), author_data['birth_date'])

    def test_retrieve_authors(self):
        response = self.client.get(path=reverse('authors-detail', args=[self.author_1.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.author_1.id)
        self.assertEqual(response.data['first_name'], self.author_1.first_name)
        self.assertEqual(response.data['last_name'], self.author_1.last_name)
        self.assertEqual(response.data['email'], self.author_1.email)
        self.assertEqual(response.data['birth_date'], self.author_1.birth_date)

    def test_update_authors(self):
        updated_data = {
            'first_name': 'Alex'
        }
        response = self.client.patch(
            reverse('authors-detail', args=[self.author_1.id]),
            data=json.dumps(updated_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(updated_data['first_name'], response.data['first_name'])

        updated_author = self.author_model.objects.get(id=self.author_1.id)

        self.assertEqual(updated_data['first_name'], updated_author.first_name)

        self.assertTrue(self.author_1.first_name != updated_author.first_name)

    def test_delete_author(self):
        response = self.client.delete(reverse('authors-detail', args=[self.author_1.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(ObjectDoesNotExist):
            deleted_author = self.author_model.objects.get(id=self.author_1.id)

    def test_books_action(self):
        book1 = self.book_model.objects.create(author=self.author_1, name='Book 1', year=2020)
        book2 = self.book_model.objects.create(author=self.author_1, name='Book 2', year=2021)

        response = self.client.get(reverse('authors-books', args=[self.author_1.id]))

        self.assertEqual(response.data[0]['id'], book1.id)
        self.assertEqual(response.data[0]['name'], book1.name)
        self.assertEqual(response.data[0]['year'], book1.year)
        self.assertEqual(response.data[0]['author_name'], book1.author.full_name)

        self.assertEqual(response.data[1]['id'], book2.id)
        self.assertEqual(response.data[1]['name'], book2.name)
        self.assertEqual(response.data[1]['year'], book2.year)
        self.assertEqual(response.data[1]['author_name'], book2.author.full_name)

    # def test_create_authors_failed(self):
    #     author_data = {
    #         'first_name': 100 * 'i',
    #         'last_name': 'Ban',
    #         'email': 'ib@gmail.com',
    #         'birth_date': '2000-01-01',
    #     }
    #     with self.assertRaises(BadRequest):
    #         response = self.client.post(reverse('authors-list'), author_data, format='json')
# import pytest
# import requests
# from django.apps import apps
# from django.urls import reverse
# from rest_framework import status
# from django.test import override_settings
#
#
# @pytest.fixture(autouse=True)
# def disable_debug_toolbar_settings():
#     with override_settings(DEBUG_TOOLBAR_CONFIG={'SHOW_TOOLBAR_CALLBACK': lambda request: False}):
#         yield
#
#
# @pytest.fixture
# def setup_data():
#     author_data_1 = {
#         'first_name': 'Petr',
#         'last_name': 'Petrov',
#         'email': 'pp@gmail.com',
#         'birth_date': '2000-01-01',
#     }
#     author_data_2 = {
#         'first_name': 'Ivan',
#         'last_name': 'Ivanov',
#         'email': 'ii@gmail.com',
#         'birth_date': '2010-01-01',
#     }
#
#     author_model = apps.get_model('rest', 'Author')
#     book_model = apps.get_model('rest', 'Author')
#
#     author_1 = author_model.objects.create(**author_data_1)
#     author_2 = author_model.objects.create(**author_data_2)
#
#     return {
#         'author_model': author_model,
#         'book_model': book_model,
#         'author_1': author_1,
#         'author_2': author_2,
#     }
#
#
# def test_list_authors(setup_data):
#     response = requests.get(reverse('authors-list'))
#     # authors = response.data
#
#     assert response.status_code == status.HTTP_200_OK
#
#     assert isinstance(authors, list)
#
#     assert len(authors) == 2
#
#     assert authors[0]['id'] == setup_data['author_1'].id
#     assert authors[0]['first_name'] == setup_data['author_1'].first_name
#     assert authors[0]['last_name'] == setup_data['author_1'].last_name
#     assert authors[0]['email'] == setup_data['author_1'].email
#     assert authors[0]['birth_date'] == str(setup_data['author_1'].birth_date)
#
#     assert authors[1]['id'] == setup_data['author_2'].id
#     assert authors[1]['first_name'] == setup_data['author_2'].first_name
#     assert authors[1]['last_name'] == setup_data['author_2'].last_name
#     assert authors[1]['email'] == setup_data['author_2'].email
#     assert authors[1]['birth_date'] == str(setup_data['author_2'].birth_date)