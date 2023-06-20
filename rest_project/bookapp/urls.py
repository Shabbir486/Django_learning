from django.urls import path
from bookapp.views import (
    BookListCreateView,
    BookRetrieveUpdateDestroyView,
    BookListView,
    BookCreateView,
    BookRetrieveView,
    BookUpdateView,
    BookDestroyView,
    getAllBooks,
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('getAll/', getAllBooks.as_view(), name='book-list-view'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-delete'),
    path('books/list/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/retrieve/', BookRetrieveView.as_view(), name='book-retrieve'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/destroy/', BookDestroyView.as_view(), name='book-destroy'),
]
