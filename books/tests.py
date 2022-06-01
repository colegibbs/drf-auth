from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import book


class BookTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_book = book.objects.create(
            name="Harry Potter",
            owner=testuser1,
            publication_date="2022-05-09",
            description="Magically Magic Stuff.",
        )
        test_book.save()

    def test_books_model(self):
        books = book.objects.get(id=1)
        actual_owner = str(books.owner)
        actual_name = str(books.name)
        actual_publication_date = str(books.publication_date)
        actual_description = str(books.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Harry Potter")
        self.assertEqual(actual_publication_date, "2022-05-09")
        self.assertEqual(
            actual_description, "Magically Magic Stuff."
        )

    def test_get_thing_list(self):
        url = reverse("book_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.data
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["name"], "Harry Potter")

    def test_get_thing_by_id(self):
        url = reverse("book_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        thing = response.data
        self.assertEqual(thing["name"], "Harry Potter")

    def test_create_thing(self):
        url = reverse("book_list")
        data = {"owner": 1, "name": "Dune","description": "Sandy.", "publication_date": "2022-05-09"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        books = book.objects.all()
        self.assertEqual(len(books), 2)
        self.assertEqual(book.objects.get(id=2).name, "Dune")

    def test_update_thing(self):
        url = reverse("book_detail", args=(1,))
        data = {
            # "id": 1,
            "owner": 1,
            "name": "Dune",
            "description": "more sandy stuff.",
            "publication_date": "2022-05-09",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = book.objects.get(id=1)
        self.assertEqual(book.name, data["name"])
        self.assertEqual(book.owner.id, data["owner"])
        self.assertEqual(book.publication_date, data["publication_date"])
        self.assertEqual(book.description, data["description"])

    def test_delete_thing(self):
        url = reverse("book_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        books = book.objects.all()
        self.assertEqual(len(books), 0)

