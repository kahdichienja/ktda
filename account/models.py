from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.


class FarmerModel(models.Model):
    """Model definition for FarmerModel."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=191)
    id_number = models.IntegerField()
    ktda_number = models.CharField(max_length=191, unique=True)
    profile = models.FileField(upload_to="userprofile")
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Unicode representation of FarmerModel."""
        return f"{self.full_name}"


TEA_TYPE_CHOICES = (
    ('PT', 'Purple Tea'),
    ('BT', 'Black Tea'),
    ('DT', 'Dark Tea'),
    ('WT', 'White Tea'),
)

class RecordModel(models.Model):
    """Model definition for FarmerModel."""

    # TODO: Define fields here
    user = models.ForeignKey(FarmerModel, on_delete=models.CASCADE)
    admin_name = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_kilo = models.DecimalField(max_digits = 8, decimal_places=2)
    price = models.DecimalField(max_digits = 8, decimal_places=2, default=16)
    tea_type = models.CharField(choices=TEA_TYPE_CHOICES, max_length=2)
    timestamp = models.DateTimeField(auto_now_add=True)





    def __str__(self):
        """Unicode representation of FarmerModel."""
        return f"{self.user}"
    
    def save(self, *args, **kwargs):
        if self.price:
            self.price = int(self.no_of_kilo) * int(16)
        
        super().save(*args, **kwargs)



    # TODO: Define custom methods here
    

    def get_system_total_kilo(self):
        ttk = RecordModel.objects.aggregate(Sum('no_of_kilo'))
        return ttk['no_of_kilo__sum']

    def get_system_total_cash(self):
        tt = RecordModel.objects.aggregate(Sum('price'))
        return tt['price__sum']

    def get_total_cash(self, request):
        tt = RecordModel.objects.filter(user=request.user.farmermodel).aggregate(Sum('price'))
        return tt['price__sum']
    def get_total_kilos(self, request):
        ttk = RecordModel.objects.filter(user=request.user.farmermodel).aggregate(Sum('no_of_kilo'))
        return ttk['no_of_kilo__sum']




