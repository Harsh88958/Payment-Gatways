from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
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


def paypage(request):
    return render(request, "paypage.html")


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
            return HttpResponse(
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
                datas = {
                    "payment_id": payment["id"],
                }
                print(datas["payment_id"])
                return render(request, "paypage.html", {"datas": datas})
        except Exception as e:
            return HttpResponse(
                {"message": f"Failed to create payment: {str(e)}"}, status=500
            )
    else:
        return HttpResponse("Please provide an amount", status=400)
