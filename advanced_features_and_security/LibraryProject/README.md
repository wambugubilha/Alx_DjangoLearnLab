# LibraryProject

LibraryProject is a foundational Django web application created to explore and understand the core structure of a Django project. This setup includes the initial configuration, development server launch, and a walkthrough of essential components like `settings.py`, `urls.py`, and `manage.py`.

## Features

- Django 4.x+ project scaffolded using `django-admin`
- Local development server setup for rapid iteration
- Clear separation of configuration and routing logic
- Ready for app creation and modular expansion

## Getting Started

To run this project locally:

```bash
python -m pip install django
python -m django startproject LibraryProject
cd LibraryProject
python manage.py runserver


# Advanced Features and Security

## Custom User Model
- Extended `AbstractUser` with `date_of_birth` and `profile_photo`.
- Integrated into admin via `CustomUserAdmin`.

## Permissions & Groups
- Defined `can_view`, `can_create`, `can_edit`, `can_delete` on `Book`.
- Used `@permission_required` decorators in views.

## Security Best Practices
- CSRF tokens in all forms.
- Secure settings in `settings.py`.
- ORM used for all queries to prevent SQL injection.

## HTTPS & Secure Redirects
- Enforced HTTPS via `SECURE_SSL_REDIRECT`.
- Configured HSTS and secure cookies.

# Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Created via management command:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

## Views
Protected using `@permission_required` decorators.

## Testing
Use Django admin to assign users to groups and verify access.

# Django Security Measures

## Configured Settings
- DEBUG = False
- Secure cookies and headers
- HTTPS enforced via SECURE_SSL_REDIRECT and HSTS

## CSRF Protection
- {% csrf_token %} added to all forms

## SQL Injection Prevention
- All queries use Django ORM
- User input validated via Django forms

## XSS Protection
- Auto-escaping in templates
- CSP headers configured via django-csp

## Testing
- Manual tests performed for CSRF, XSS, and SQL injection
