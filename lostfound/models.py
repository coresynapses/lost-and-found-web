from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    def searchItem(self,query):
        return Item.objects.filter(itemName__icontains=query) | Item.objects.filter(description__icontains=query)
    
    def claimItem(self, item, proofDescription):
        if item.status == Item.Lost:
            item.status = Item.underReview
            item.proofOfOwnership = proofDescription
            item.claimer = self
            item.save()
            return f"The item, {item.itemName} has been submitted to admin for verification."
        else:
            return "Item is not lost."
        
    def reportLostItem(self, itemName,description, category,location, photoUpload,contactInfo):
        lostItem = Item.objects.create(
            itemName = itemName,
            description = description,
            category = category,
            location = location,
            photo = photoUpload,
            contactInfo = contactInfo,
            status = Item.Lost,
        )
        return f"Lost item '{lostItem.itemName}' reported successfully."

    def reportFoundItem(self, itemName,description, category,location, photoUpload,contactInfo):
        foundItem = Item.objects.create(
            itemName = itemName,
            description = description,
            category = category,
            location = location,
            photo = photoUpload,
            contactInfo = contactInfo,
            status = Item.Found,
        )
        return f"Found item '{foundItem.itemName}' reported successfully."

class Category(models.Model):
    categoryName = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryName

class Item(models.Model):
    Lost = "Lost"
    Found = "Found"
    underReview = "Under Review"
    STATUS_CHOICES = [
        (Lost, "Lost"),
        (Found, "Found"),
        (underReview, "Under Review"),
    ]

    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField("Item Name", max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, null= True, default=1,on_delete=models.CASCADE)
    dateReported = models.DateTimeField("Date Reported", auto_now_add=True)
    dateClaimed = models.DateTimeField("Date Claimed", null= True, blank=True)
    location = models.CharField(max_length=255)
    photo = models.ImageField(upload_to= 'item_photos/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=Lost)
    contactInfo = models.CharField("Contact Information",max_length=255)
    proofOfOwnership = models.TextField("Proof of Ownership",blank=True, null=True)
    claimer = models.ForeignKey(CustomUser, null= True, blank = True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return f"{self.itemName} ({self.get_status_display()})"

class Report(models.Model):
    reportID = models.AutoField(primary_key=True)
    reportedItems = models.ManyToManyField(Item)

    def get_content(self):
        return "\n".join([
            f"Item: {item.itemName}\n"
            f"Status: {item.status}\n"
            f"Date Reported: {item.dateReported}\n"
            f"Category: {item.category.categoryName}\n"
            for item in self.reportedItems.all()
        ])