# Author model stores writer's name.
# Each Author can have multiple Books (one-to-many relationship).

# Book model includes title, publication year, and a foreign key to Author.
# BookSerializer serializes all fields and validates publication_year.
# AuthorSerializer includes nested BookSerializer to show related books.
