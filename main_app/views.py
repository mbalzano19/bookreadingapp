from django.shortcuts import render, redirect
from .models import Child, Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from .data import data
from .forms import ChildForm


# Create your views here.
# data = data()

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html',{'books': books})

def books_detail(request,book_id):
    books = Book.objects.filter(id=book_id)
    return render(request, 'books/detail.html',{'book': books})


@login_required
def children_index(request):
    children = Child.objects.all()
    return render(request, 'children/index.html', {
        'children': children
    })

# @login_required
# def children_detail(request, child_id):
#     child = Child.objects.get(id=child_id)
#     books = Book.objects.filter(user=request.user)
#     return render(request, 'children/detail.html', {
#         'child': child,
#         'books': books
#     })

@login_required
def children_detail(request, child_id):
    child = Child.objects.get(id=child_id)
    id_list = child.books.all().values_list('id')
    books_child_doesnt_have = Book.objects.exclude(id__in=id_list)
    return render(request, 'children/detail.html', {
        'child': child,
        'books': books_child_doesnt_have
    })




class ChildCreate(CreateView):
    model = Child
    fields = ['name', 'age_group']
    success_url = '/children'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# def add_child(request, user_id):
#   form = ChildForm(request.POST)
#   if form.is_valid():
#     new_child = form.save(commit=False)
#     new_child.user_id = user_id
#     new_child.save()
#   return redirect('detail', user_id=user_id)


class ChildUpdate(UpdateView):
    model = Child
    fields = ['age_group']

class ChildDelete(DeleteView):
    model = Child
    success_url = '/children'

@login_required
def assoc_book(request,child_id, book_id):
    Child.objects.get(id=child_id).books.add(book_id)
    return redirect('detail', child_id=child_id)

@login_required
def disassoc_book(request, child_id, book_id):
    Child.objects.get(id=child_id).books.remove(book_id)
    return redirect('detail', child_id=child_id)

class BookList(LoginRequiredMixin,ListView):
  model = Book

class BookDetail(LoginRequiredMixin,DetailView):
  model = Book

def signup(request):
    print(request)
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again. Go home.'
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
