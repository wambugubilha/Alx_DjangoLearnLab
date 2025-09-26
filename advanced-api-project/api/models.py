from django.db import models
# Author model: stores author names.
class Author(models.Model):
    name = models.CharField(max_length=100)
    # Represents a writer who can have multiple books

    def __str__(self):
        return self.name
# Book model: stores book details and links each book to an author.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # Each book is linked to one author

    def __str__(self):
        return f"{self.title} ({self.publication_year})"