The BookListView is configured using ListAPIView. It retrieves all book records from the database and is accessible to both authenticated and unauthenticated users.

The BookDetailView is built with RetrieveAPIView. It returns detailed information about a specific book identified by its primary key. This view is publicly accessible.

The BookCreateView uses CreateAPIView. It allows authenticated users to submit new book entries. The view enforces validation rules defined in the BookSerializer, including a check that the publication year is not in the future.

The BookUpdateView is implemented with UpdateAPIView. It enables authenticated users to modify existing book records. It inherits validation logic from the serializer and can be extended to include custom update behavior.

The BookDeleteView is configured with DestroyAPIView. It allows authenticated users to delete a book instance from the database. This view can be restricted further using custom permission classes.


All views use the BookSerializer to handle data serialization and validation. The serializer ensures that the publication year is valid and formats the book data for API responses.

Permissions are enforced using Django REST Framework’s built-in classes. AllowAny is used for read-only views (ListView and DetailView), while IsAuthenticated is applied to write operations (CreateView, UpdateView, and DeleteView).

URL routing is defined in api/urls.py, with each view mapped to a distinct endpoint. For example, /api/books/ maps to the list view, and /api/books/<int:pk>/update/ maps to the update view.

Each view is designed to be modular and extensible. Developers can override methods like perform_create() or get_queryset() to customize behavior further.

Manual testing is recommended using tools like Postman or curl. Each endpoint should be tested for correct data handling, validation, and permission enforcement.

These views form the backbone of the API’s CRUD functionality and are structured to support future enhancements such as filtering, searching, and ordering.

## Filtering, Searching, and Ordering

The `BookListView` supports advanced query capabilities:

- **Filtering**: Use query parameters like `?title=`, `?author=`, `?publication_year=` to filter results.
- **Searching**: Use `?search=` to search by book title or author name.
- **Ordering**: Use `?ordering=title` or `?ordering=-publication_year` to sort results.

These features are powered by DjangoFilterBackend, SearchFilter, and OrderingFilter.
