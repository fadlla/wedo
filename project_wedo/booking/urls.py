from django.urls import path
from . import views



urlpatterns = [
    path('contacts/inquiry/', views.inquiry, name='inquiry'),
  # URL untuk membuat pembayaran
    path('make_payment/<int:inquiry_id>/', views.make_payment, name='make_payment'),

    # URL untuk mengunggah bukti pembayaran
    path('upload_proof/<int:inquiry_id>/', views.upload_proof, name='upload_proof'),

    # URL untuk pembayaran "Bayar di Tempat"
    path('bayar_di_tempat/<int:inquiry_id>/', views.bayar_di_tempat, name='bayar_di_tempat'),
    
    path('validate_payment/<int:inquiry_id>/', views.validate_payment, name='validate_payment'),
    # ...kode URL lainnya...
    path('print_receipt/<int:inquiry_id>/', views.print_receipt, name='print_receipt'),
]





