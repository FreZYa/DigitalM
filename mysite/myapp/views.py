from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Product, OrderDetail
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
from django.http import JsonResponse
from django.http import HttpResponseNotFound

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "myapp/index.html", {"products": products})

def detail(request, id):
    product = Product.objects.get(id=id)
    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, "myapp/detail.html", {"product": product, "stripe_publishable_key": stripe_publishable_key})

@csrf_exempt
def create_checkout_session(request, id):
    request_data = json.loads(request.body)
    product = Product.objects.get(id=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        customer_email=request_data['email'],
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url = request.build_absolute_uri(reverse('success')) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url = request.build_absolute_uri(reverse('failed'))
    )
    order_detail = OrderDetail.objects.create(
        customer_email=request_data['email'],
        product=product,
        amount=int(product.price),
        stripe_session_id=checkout_session.id,
    )
    order_detail.save()
    return JsonResponse({'sessionId': checkout_session.id})

def payment_success_view(request):
    session_id = request.GET.get('session_id')
    if session_id is None:
        return HttpResponseNotFound()
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.retrieve(session_id)
    
    # Get the payment intent from the session if available
    payment_intent = session.payment_intent if hasattr(session, 'payment_intent') else None
    
    # Find order by session id instead of payment intent
    order = get_object_or_404(OrderDetail, stripe_session_id=session_id)
    
    # Update payment intent if available
    if payment_intent:
        order.stripe_payment_intent = payment_intent
    
    order.has_paid = True
    order.save()
    return render(request, "myapp/payment_success.html", {"order": order})

def payment_failed_view(request):
    return render(request, "myapp/failed.html")