from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied

from .models import CustomUser, Item, claimRequestReport, fraudClaimReport  # Ensure all models are imported
from .forms import CustomUserCreationForm, ItemForm, claimForm, fraudForm

def homepage(request):
    return render(request, 'homepage.html')

def loginPage(request):
    return HttpResponse("This is the login page.")

def registerUser(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('itemList')
        else:
            form = CustomUserCreationForm()
        return render(request, "registration/", {"form": form}) #needs HTML 

#lists all items
def itemList(request): 
    item = Item.objects.all().values(
        'itemName',
        'status',
        'dateReported',
        'category__categoryName',
    )
    
    return render(request, '', {'item': item}) #needs HTML

#provides details on one item, and can claim or report fraud on item.
def itemDetail(request, item_id): 
    item = get_object_or_404(Item, id=item_id)

    isClaimed = claimRequestReport.objects.filter(item=item, status = "Approved").exists()

    itemClaim = "Claim Item" if not isClaimed else "Report as Fraudulent"


    context = {
        'item': item,
        'isClaimed' : isClaimed,
        'itemClaim' : itemClaim,
    }

    return render(request, '', context) #needs HTML

#item creation
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('itemDetail')
    else:
        form = ItemForm()
    return render(request, 'lostfound/add_item.html', {'form': form})

# edit item
def editItem(request, item_id):
    item = get_object_or_404(Item, id = item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance= item)
        if form.is_valid():
            form.save()
            return redirect('itemDetail')
    else:
        form = ItemForm(instance = item)
    
    return render(request, '', {'form': form, 'item': item})#needs HTML

#item deletion
def deleteItem(request, item_id):
    item = get_object_or_404(Item, id = item_id)

    if request.method == 'POST':
        if 'confirm' in request.POST:
            item.delete()
            return redirect('itemList')
        else:
            return redirect('itemDetail', item_id = item.id)
    
    return render(request, '', {'item': item}) #needs HTML

#claims creation
def claimRequest(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = claimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.item= item
            claim.claimer = request.user
            claim.save()
            return redirect('itemDetail')
    else:
        form = claimForm()

    return render(request,'' ,{'form': form, 'item': item}) #needs HTML

#edit claim
def editClaim(request, claim_id):
    claim = get_object_or_404(claimRequestReport, id = claim_id)

    if claim.claimer != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = claimForm(request.POST, instance=claim)
        if form.is_valid():
            form.save()
            return redirect('itemDetail', item_id= claim.item.id)
    else:
        form = claimForm(instance=claim)

    return render(request, '', {'form': form, 'claim' : claim}) #needs HTML

#delete claim
def deleteClaim(request, claim_id):
    claim = get_object_or_404(claimRequestReport, id = claim_id)

    if claim.claimer != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            claim.delete()
            return redirect('itemDetail', item_id = claim.item.id)
    
        else:
            return redirect('itemDetail', item_id=claim.item.id)
    
    return render(request, '', {'claim': claim}) #needs HTML

#fraud creation
def fraudReport(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = fraudForm(request.POST)
        if form.is_valid():
            fraud = form.save(commit=False)
            fraud.item = item
            fraud.reporter = request.user
            fraud.save()
            return redirect('itemDetail')
    else: 
        form = fraudForm()
    
    return render(request,'',{'form':form, 'item': item}) #needs HTML

#edit fraud claim
def editFraud(request, fraud_id):
    fraud = get_object_or_404(fraudClaimReport, id = fraud_id)
    
    if fraud.reporter != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = fraudForm(request.POST, instance=fraud)
        if form.is_valid():
            form.save()
            return redirect('itemDetail', item_id= fraud.item.id)
        
    else: 
        form = fraudForm(instance=fraud)

    return render(request, '', {'form': form, 'fraud': fraud})

#delete fraud claim
def deleteFraud(request, fraud_id):
    fraud = get_object_or_404(fraudClaimReport, id = fraud_id)

    if fraud.reporter != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            fraud.delete()
            return redirect('itemDetail', item_id= fraud.item.id)
        else:
            return redirect('itemDetail', item_id=fraud.item.id)
    
    return render(request, '', {'fraud': fraud})

#admin related views
'''
def approveClaim():
def rejectClaim():
def resolveFraud():
def rejectFraud():
'''

