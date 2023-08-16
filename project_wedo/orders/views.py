from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Approval, Transaction
from datetime import date

# def dashboard(request):
#     user = request.user
#     orders = Order.objects.filter(user=user)
#     context = {'orders': orders}
#     return render(request, 'dashboard.html', context)

def approve_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    approval, created = Approval.objects.get_or_create(order=order)
    approval.is_approved = True
    approval.save()

    if created:
        transaction = Transaction.objects.create(order=order, transaction_date=date.today())
        # Lakukan apa pun yang diperlukan saat membuat transaksi

    return redirect('dashboard')

def create_transaction(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    transaction = Transaction.objects.create(order=order, transaction_date=date.today())
    # Lakukan apa pun yang diperlukan saat membuat transaksi

    return redirect('dashboard')
from django.shortcuts import render
from .models import Order

def dashboard(request):
    # Ambil pesanan untuk pengguna yang sedang login
    orders = Order.objects.filter(user=request.user)

    context = {
        'orders': orders
    }

    return render(request, 'dashboard.html', context)

