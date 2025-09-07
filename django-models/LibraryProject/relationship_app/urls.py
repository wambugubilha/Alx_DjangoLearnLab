from django.urls import path, include
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('', include('relationship_app.urls')),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('auth/', include('relationship_app.urls')),

]
