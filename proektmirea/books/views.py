from django.shortcuts import render

def books_fri_e(request):
    return render(request, 'main/book_development_socialism_from_utopia_to_science.html')

def books_kar_m(request):
    return render(request, 'main/book_principles_of_communism.html')

def books_ily_l(request):
    return render(request, 'main/book_where_to_begin.html')