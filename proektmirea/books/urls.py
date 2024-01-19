from django.urls import path
from . import views

urlpatterns = [
    path('book_development_socialism_from_utopia_to_science.html', views.books_fri_e, name = "books_fri_e"),
    path('book_principles_of_communism.html', views.books_kar_m, name = "books_kar_m"),
    path('book_where_to_begin.html', views.books_ily_l, name = "books_ily_l"),
]
