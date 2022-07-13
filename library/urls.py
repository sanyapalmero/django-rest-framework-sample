from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("books/", views.books_list),
    path("books/<int:pk>/", views.book_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
