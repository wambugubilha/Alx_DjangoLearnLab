from django.urls import path, include
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('', include('relationship_app.urls')),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('auth/', include('relationship_app.urls')),
    path('books/add_book/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit_book/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete_book/', views.delete_book, name='delete_book'),

]
