from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import Item, Category
from .forms import ItemForm

def index(request):
    return HttpResponse("Hello, world. You're at the lostfound index.")

def index(request):
    items = Item.objects.all()
    return render(request, 'lostfound/index.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()
    return render(request, 'lostfound/add_item.html', {'form': form})
