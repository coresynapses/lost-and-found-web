from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.conf import settings

from .models import CustomUser, Item, claimRequestReport, fraudClaimReport  # Ensure all models are imported
from .forms import CustomUserCreationForm, ItemForm, claimForm, fraudForm

#authentication & homepage
def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('lostfound:login')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or Password")
            return redirect('lostfound:login')
        else:
            login(request, user)
            return redirect(reverse('lostfound:itemList'))

    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("User registered:", user)  # Debugging
            login(request, user)
            return redirect(reverse('lostfound:itemList'))
        else:
            print("Form errors:", form.errors)  # Debugging
            messages.error(request,'Invalid username or password')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html',{"form": form})

def logout_user(request):
    logout(request)
    return redirect('lostfound:home')



#item CRUD
#lists all items and filters through item name, or description
def itemList(request):
    query = request.GET.get('query')
    if query:
        items = Item.objects.filter(itemName__icontains=query) | Item.objects.filter(description__icontains=query)
    else:
        items = Item.objects.all()
    
    return render(request, 'index.html', {
        'items': items,
        'MEDIA_URL': settings.MEDIA_URL,
        'query': query,
    })

#provides details on one item, and can claim or report fraud on item.
def itemDetail(request, item_id): 
    item = get_object_or_404(Item, itemID = item_id)

    return render(request, 'item_detail.html', {
        'item' : item,
    })

#item creation, only members can create a report, 
#if they are not logged in it will redirect them to the login page
@login_required(login_url='lostfound:login')
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return redirect('lostfound:itemDetail', item_id = item.itemID)
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

# edit item
@login_required(login_url='lostfound:login')
def editItem(request, item_id):
    item = get_object_or_404(Item, itemID = item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance= item)
        if form.is_valid():
            item = form.save()
            return redirect('lostfound:itemDetail',item_id = item.itemID)
    else:
        form = ItemForm(instance = item)
    
    return render(request, '', {'form': form, 'item': item})#needs HTML

#item deletion
@login_required(login_url='lostfound:login')
def deleteItem(request, item_id):
    item = get_object_or_404(Item, itemID = item_id)

    if request.method == 'POST':
        if 'confirm' in request.POST:
            item.delete()
            return redirect('lostfound:itemList')
        else:
            return redirect('lostfound:itemDetail', item_id = item.itemID)
    
    return render(request, '', {'item': item}) #needs HTML




#Claims CRUD
#claims creation
@login_required(login_url='lostfound:login')
def claimRequest(request, item_id):
    item = get_object_or_404(Item, itemID=item_id)

    if request.method == 'POST':
        form = claimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.item= item
            claim.claimer = request.user
            claim.save()
            return redirect('lostfound:itemDetail')
    else:
        form = claimForm()

    return render(request,'' ,{'form': form, 'item': item}) #needs HTML

#edit claim
@login_required(login_url='lostfound:login')
def editClaim(request, claim_id):
    claim = get_object_or_404(claimRequestReport, id = claim_id)

    if claim.claimer != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = claimForm(request.POST, instance=claim)
        if form.is_valid():
            form.save()
            return redirect('lostfound:itemDetail', item_id= claim.item.id)
    else:
        form = claimForm(instance=claim)

    return render(request, '', {'form': form, 'claim' : claim}) #needs HTML

#delete claim
@login_required(login_url='lostfound:login')
def deleteClaim(request, claim_id):
    claim = get_object_or_404(claimRequestReport, id = claim_id)

    if claim.claimer != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            claim.delete()
            return redirect('lostfound:itemDetail', item_id = claim.item.id)
    
        else:
            return redirect('lostfound:itemDetail', item_id=claim.item.id)
    
    return render(request, '', {'claim': claim}) #needs HTML



#Fraud CRUD
#fraud creation
@login_required(login_url='lostfound:login')
def fraudReport(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = fraudForm(request.POST)
        if form.is_valid():
            fraud = form.save(commit=False)
            fraud.item = item
            fraud.reporter = request.user
            fraud.save()
            return redirect('lostfound:itemDetail')
    else: 
        form = fraudForm()
    
    return render(request,'',{'form':form, 'item': item}) #needs HTML

#edit fraud claim
@login_required(login_url='lostfound:login')
def editFraud(request, fraud_id):
    fraud = get_object_or_404(fraudClaimReport, id = fraud_id)
    
    if fraud.reporter != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = fraudForm(request.POST, instance=fraud)
        if form.is_valid():
            form.save()
            return redirect('lostfound:itemDetail', item_id= fraud.item.id)
        
    else: 
        form = fraudForm(instance=fraud)

    return render(request, '', {'form': form, 'fraud': fraud})

#delete fraud claim
@login_required(login_url='lostfound:login')
def deleteFraud(request, fraud_id):
    fraud = get_object_or_404(fraudClaimReport, id = fraud_id)

    if fraud.reporter != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            fraud.delete()
            return redirect('lostfound:itemDetail', item_id= fraud.item.id)
        else:
            return redirect('lostfound:itemDetail', item_id=fraud.item.id)
    
    return render(request, '', {'fraud': fraud})

#admin related views
'''
def approveClaim():
def rejectClaim():
def resolveFraud():
def rejectFraud():
'''

