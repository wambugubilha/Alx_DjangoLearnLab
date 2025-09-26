from rest_framework import serializers
from .models import Author, Book
from datetime import datetime
# BookSerializer: serializes all fields of Book and validates publication_year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
# AuthorSerializer: includes nested BookSerializer to show all books by an author.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    # Nested serialization of related books

    class Meta:
        model = Author
        fields = ['name', 'books']
