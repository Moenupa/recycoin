from django.db import models
from accounts.models import CustomUser

# Create your models here.
class RecycoinModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recycled_coins')
    amount = models.IntegerField(default=0)
    recycledAmount = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    
class PrizeModel(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=256)
    img = models.CharField(max_length=256)
    price = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    
class ExchangeRecordModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='exchanged_records')
    amount = models.IntegerField(default=0)
    prize = models.ForeignKey(PrizeModel, on_delete=models.CASCADE, related_name='exchanged_records')
    time = models.DateTimeField(auto_now_add=True)