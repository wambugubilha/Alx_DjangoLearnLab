from django.contrib import admin
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

author = Author.objects.create(name="Chinua Achebe")
book = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=author)

# Serialize
serializer = AuthorSerializer(author)
print(serializer.data)
