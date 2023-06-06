from django.shortcuts import render
from .models import Child
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .form import ChildForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def children_index(request):
    children = Child.objects.all()
    return render(request, 'children/index.html', {
        'children': children
    })

def children_detail(request, child_id):
    child = Child.objects.get(id=child_id)
    childform = ChildForm()
    return render(request, 'children/detail.html', {
        'child': child,
        'childform':childform
    })

class ChildCreate(CreateView):
    model = Child
    fields = '__all__'
    success_url = '/children'

class ChildUpdate(UpdateView):
    model = Child
    fields = ['age_group']

class ChildDelete(DeleteView):
    model = Child
    success_url = '/children'
    
