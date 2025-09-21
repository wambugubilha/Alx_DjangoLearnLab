# api/urls.py
from django.urls import path
from .views import BookList
from django.urls import  include
from rest_framework.routers import DefaultRouter
from .views import  BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # CRUD routes from ViewSet
]
