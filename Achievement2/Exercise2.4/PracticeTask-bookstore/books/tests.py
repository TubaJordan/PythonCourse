from django.test import TestCase
from .models import Book #to access Book model

# Create your tests here.

class BookModelTest(TestCase):
    def setUpTestData():
        #Set up non-modifed objects used by all test methods
        Book.objects.create(name="Pride and Prejudice", author_name="Jane Austen", genre="classic", book_type="hardcover", price="23.71")


    def test_book_name(self):
        #get a book obejct to test
        book = Book.objects.get(id=1)

        #get the metadata from the "name" firld and use it to query its data
        field_label = book._meta.get_field("name").verbose_name

        #compare the value to the expected result
        self.assertEqual(field_label, "name")


    def test_author_name_max_length(self):
        #get a book object to test
        book = Book.objects.get(id=1)

        #get the metadata fro the "author_name" field and use it to query its max_length
        max_length = book._meta.get_field("author_name").max_length

        #compare the vlaue to the expected result i.e. 120
        self.assertEqual(max_length, 120)