from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy

from .models import Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 8
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    def get_queryset(self):
        return Book.objects.order_by('datetime_added')

# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'
#     context_object_name = 'book'

def book_detail_view(request, pk):
    # get book object
    book = get_object_or_404(Book, pk=pk)
    # get book comment
    comments = book.comments.all()
    return render(request, 'books/book_detail.html', {'book': book, 'comments': comments})

class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'translator', 'publisher', 'content', 'pages', 'price', 'cover', 'status']
    template_name = 'books/book_create.html'

class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'translator', 'publisher', 'content', 'pages', 'price', 'cover', 'status']
    template_name = 'books/book_update.html'

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
