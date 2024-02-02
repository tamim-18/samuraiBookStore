from django.contrib import admin
from django.urls import path, include
from .views import BooksAPIView, BookDetailAPIView

app = 'api'
urlpatterns = [
    path(
        route='books/',
        view=BooksAPIView.as_view(),
        name='books-list',
    ),
    path(
        route='books/<int:pk>/',
        view=BookDetailAPIView.as_view(),
        name='books-detail',
    ),
]
