from django.shortcuts import HttpResponse, render, redirect
from .models import Item, Category, Report  # Ensure all models are imported
from .forms import ItemForm

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

def reportList(request):
    reports = Report.objects.all()
    return render(request, 'reportList.html', {'Reports': reports})
