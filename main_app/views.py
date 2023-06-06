from django.shortcuts import render, redirect
from .models import Child
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
<<<<<<< HEAD
from .form import ChildForm
=======
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .data import data
>>>>>>> main


# Create your views here.
data = data()

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def children_index(request):
    children = Child.objects.all()
    return render(request, 'children/index.html', {
        'children': children
    })

@login_required
def children_detail(request, child_id):
    child = Child.objects.get(id=child_id)
    childform = ChildForm()
    return render(request, 'children/detail.html', {
        'child': child,
        'childform':childform
    })

class ChildCreate(CreateView):
    model = Child
    fields = ['name', 'age_group']
    success_url = '/children'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ChildUpdate(UpdateView):
    model = Child
    fields = ['age_group']

class ChildDelete(DeleteView):
    model = Child
    success_url = '/children'
<<<<<<< HEAD
    
=======

def signup(request):
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
>>>>>>> main
