# blog/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, add_comment, CommentUpdateView, CommentDeleteView

)
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:post_id>/comments/new/", add_comment, name="comment-add"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-update"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]

