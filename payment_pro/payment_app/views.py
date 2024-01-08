from django.shortcuts import render
from django.http import JsonResponse
from razorpay.errors import BadRequestError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import razorpay, uuid
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import IntegrityError

# Create your views here.


def index(request):
    return render(request, "payment.html")


def create(request):
    if request.GET.get("amount"):
        key_id = "rzp_test_QOxL4qlbdniQb8"
        secret = "JXvQxiwXLOgyxOFxQvGiFMQj"
        amount = request.GET.get("amount")
        try:
            amount = int(amount)
            print(amount)
        except (TypeError, ValueError):
            print("Please provide a valid amount")
            return JsonResponse(
                {"message": "Please provide a valid amount"}, status=400
            )
        client = razorpay.Client(auth=(key_id, secret))
        receipt_id = str(uuid.uuid4())
        payload = {
            "amount": amount * 100,
            "currency": "INR",
            "receipt": receipt_id,
        }
        try:
            payment = client.order.create(data=payload)
            # payment = "order_NHklJYkAUZ7Fxo"
            data = Payment.objects.filter(order_id=payment).values()
            if data:
                return render(request, "templates/error.html")
            else:
                data = Payment.objects.create(
                    order_id=payment["id"],
                    amount=float(payment["amount"] / 100),
                    currency=payment["currency"],
                    status=payment["status"],
                )
                return JsonResponse({"data": payment[id]})
        except Exception as e:
            return Response(
                {"message": f"Failed to create payment: {str(e)}"}, status=500
            )
