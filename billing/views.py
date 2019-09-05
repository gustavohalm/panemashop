from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ( TemplateView, ListView, DetailView,CreateView, UpdateView)
from portal import models
from .models import Order
from . import forms
from .services import BillingServices
# Create your views here.
def payment(request, slug):
    product = get_object_or_404(models.Product, slug=slug)
    message = ''
    if request.method == 'POST':
        form = forms.PaymentForm( request.POST)
        if form.is_valid():
            payment_data = {

                'number': form.cleaned_data['credit_card_number'],
                'verification_value' : form.cleaned_data['credit_card_cvv'],
                'first_name': form.cleaned_data['credit_card_first_name'],
                'last_name': form.cleaned_data['credit_card_last_name'],
                'month': form.cleaned_data['credit_card_month'],
                'year': form.cleaned_data['credit_card_year'],
            }
            billing = BillingServices()
            order = billing.charge(request.user, product, payment_data)
            if order:
                return redirect("item_purchased", order.id)
            else:
                message = 'Não foi possivel realizar a compra. Confira os dados inseridos!'

    form = forms.PaymentForm()
    content = {
        'form':form,
        'product':product,
        'message': message
    }

    return render(request, 'payment/payment.html', content)

def item_purchased(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if order.user != request.user:
        return  redirect('home')
    context = {
        'order': order
    }
    return render(request, "payment/item_purchased.html", context)

class UserSales(ListView):
    model = Order
    template_name = 'payment/list_orders.html'
    def get_queryset(self):
        return Order.objects.filter(merchant=self.request.user)

def salesUpdate(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if ( request.user ):
        if ( order.merchant != request.user ):
                return redirect( '../../')
    else:
        return redirect('../../')

    form = forms.OrderForm()
    if 'shipment' in request.POST:
        new_shipment = request.POST['shipment']
        order.shipment = new_shipment

    context = {
        'order': order,
        'form' : form
    }
    return render(request, 'payment/update_order.html', context)


class UsersShopping(ListView):
    model = Order
    template_name = 'payment/list_shopping.html'
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
