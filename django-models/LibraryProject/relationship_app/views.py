from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.contrib import messages
from .models import Book
from .models import Library

# ✅ Function-based view: List all books
def list_books(request):
    books = Book.objects.all()  # Explicitly using Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Explicit template path

# ✅ Class-based view: Library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace with your actual home view
        else:
            messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Registration failed")
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})