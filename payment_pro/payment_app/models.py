from django.db import models


# Create your models here.
class Payment(models.Model):
    payment_id = models.CharField(max_length=400, null=True, blank=True)
    order_id = models.CharField(max_length=400, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=200, null=True, blank=True)
    method = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    created_at = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.order_id
