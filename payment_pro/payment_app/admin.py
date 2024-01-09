from django.contrib import admin

# Register your models here.
from .models import *


# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "payment_id",
        "order_id",
        "amount",
        "currency",
        "method",
        "status",
        "email",
        "contact",
        "created_at",
    )
    list_filter = ("status", "currency", "method")
    search_fields = ("payment_id", "order_id", "email")
    list_per_page = 20
    ordering = ("-created_at",)


@admin.register(Phonepe)
class PhonepeAdmin(admin.ModelAdmin):
    list_display = (
        "status",
        "amount",
        "merchant_transaction_id",
        "transaction_id",
        "created_at",
    )
    search_fields = ("status", "merchant_transaction_id", "transaction_id")
    list_filter = ("status", "payment_type")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
