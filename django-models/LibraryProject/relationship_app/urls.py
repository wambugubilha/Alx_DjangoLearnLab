from django.urls import path, include
from .views import list_books, LibraryDetailView

urlpatterns = [
     path('', include('relationship_app.urls')),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
