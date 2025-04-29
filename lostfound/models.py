from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    def searchItem(self,query):
        return Item.objects.filter(itemName__icontains=query) | Item.objects.filter(description__icontains=query)
    
    def claimItem(self, item, itemName,proofDescription, contactInfo):
        if item.status == Item.found:
            item.status = Item.underReview
            item.save()

            claimRequest = claimRequestReport.objects.create(
                itemName = itemName,
                claimer = self,
                proofOfOwnership = proofDescription,
                contactInfo = contactInfo,
                status= claimRequestReport.pending,
            )
            return f"The claim request for '{claimRequest.itemName}' has been submitted for verification."
        else:
            return "Lost items cannot be claimed."
        
    def reportLostItem(self, itemName,description, category,location, photoUpload,contactInfo):
        lostItem = Item.objects.create(
            itemName = itemName,
            description = description,
            category = category,
            location = location,
            photo = photoUpload,
            contactInfo = contactInfo,
            status = Item.lost,
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
            status = Item.found,
        )
        return f"Found item '{foundItem.itemName}' reported successfully."

class Category(models.Model):
    categoryID   = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryName

class Item(models.Model):
    lost = "Lost"
    found = "Found"
    underReview = "Under Review"
    claimed = "Claimed"
    unclaimed = 'Unclaimed'

    STATUS_CHOICES = [
        (lost, "Lost"),
        (found, "Found"),
    ]

    DISPOSITION_CHOICES = [
        (underReview, "Under Review"),
        (claimed, "Claimed"),
        (unclaimed, "Unclaimed"),
    ]

    itemID           = models.AutoField    (primary_key=True)
    itemName         = models.CharField    ("Item Name", max_length=255, default="")
    description      = models.TextField    (blank=True, null=True, default="")
    category         = models.ForeignKey   (Category, null= True, default=1,on_delete=models.CASCADE)
    dateReported     = models.DateTimeField("Date Reported", auto_now_add=True)
    dateClaimed      = models.DateTimeField("Date Claimed", null= True, blank=True)
    location         = models.CharField    (max_length=255,blank=True, null=True )
    photo            = models.ImageField   (upload_to= 'item_photos/', null=True, blank=True)
    status           = models.CharField    (max_length=20, choices=STATUS_CHOICES, default=lost)
    disposition      = models.CharField    (max_length=20,choices=DISPOSITION_CHOICES,default=unclaimed)
    contactInfo      = models.CharField    ("Contact Information (Email)",max_length=255, default="")
    proofOfOwnership = models.TextField    ("Proof of Ownership",blank=True, null=True)
    claimer          = models.ForeignKey   (CustomUser, null= True, blank = True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Item"
    

    def __str__(self):
        return f"{self.itemName} ({self.get_status_display()})"

class claimRequestReport(models.Model):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"

    STATUS_CHOICES = [
        (pending, "Pending"),
        (approved, "Approved"),
        (rejected, "Rejected"),
    ]

    claimID          = models.AutoField    (primary_key=True)
    item             = models.OneToOneField(Item, on_delete=models.CASCADE)
    claimer          = models.ForeignKey   (CustomUser, on_delete=models.CASCADE, related_name="claimUser")
    contactInfo      = models.CharField    ("Contact Information",max_length=255, default="")
    proofOfOwnership = models.TextField    ("Proof of Ownership",default="")
    status           = models.CharField    (max_length=20, choices=STATUS_CHOICES, default=pending)
    reviewAdmin      = models.ForeignKey   (CustomUser, null= True, blank= True, on_delete=models.SET_NULL, related_name="claimAdminUser")
    dateSubmitted    = models.DateTimeField("Date Submitted",auto_now_add=True)
    dateReviewed     = models.DateTimeField("Date Reviewed", null= True, blank=True)

    class Meta:
        verbose_name = "Claim Request"

    def approveClaim(self, adminUser):

        if not self.item:
            print("Error, No Item found.")
            return
        print(f"Approving claim for: {self.item.itemName}")

        self.status = self.approved
        self.item.disposition = Item.claimed
        self.item.claimer = self.claimer
        self.item.dateClaimed = timezone.now()
        self.item.save()
        print(f"Item updated to: {self.item.disposition}")

        self.reviewAdmin = adminUser
        self.dateReviewed = timezone.now()
        self.save()
        return f"Claim for '{self.item.itemName}' has been approved and marked as {self.status}."
    
    def rejectClaim(self, adminUser):
        self.status = self.rejected
        self.item.disposition = Item.unclaimed
        self.item.save()
        self.reviewAdmin = adminUser
        self.dateReviewed = timezone.now()
        self.save()

        return f"Claim for '{self.item.itemName}' has been rejected."
    
    def __str__(self):
        return f"Claim Request for {self.item.itemName} - {self.status}"
    
class fraudClaimReport(models.Model):
    pending = "Pending"
    resolved = "Resolved"
    rejected = "Rejected"

    STATUS_CHOICES = [
        (pending, "Pending"),
        (resolved, "Resolved"),
        (rejected, "Rejected"),
    ]

    fraudID = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="reportUser")
    contactInfo = models.CharField("Contact Information",max_length=255, default="")
    proofOfOwnership = models.TextField("Proof of Ownership", default="")
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default=pending)
    reviewAdmin = models.ForeignKey(CustomUser, null = True, blank=True, on_delete=models.SET_NULL,related_name="reportAdminUser")
    dateSubmitted = models.DateTimeField(auto_now_add=True)
    dateReviewed = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Fraudulent Claim"

    def resolveFraud(self, adminUser):
        self.status = self.resolved
        self.item.disposition = Item.claimed
        self.item.save()
        self.reviewAdmin = adminUser
        self.dateReviewed = timezone.now()
        self.save()

        return f"Fraud claim for '{self.item.itemName}' has been resolved."
    
    def rejectFraud(self, adminUser):
        self.status = self.rejected
        self.item.disposition = Item.claimed
        self.item.save()
        self.reviewAdmin = adminUser
        self.dateReviewed = timezone.now()
        self.save()
        return f"Fraud claim for '{self.item.itemName}' has been rejected."
    
    def __str__(self):
        return f"Fraud claim for {self.item.itemName} - {self.status}"
    
