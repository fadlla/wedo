from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Bookings

def inquiry(request):
    if request.method == 'POST':
        wedding_id = request.POST['wedding_id']
        Paket = request.POST['Paket']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        No_HP = request.POST['No_HP']
        Tanggal = request.POST['Tanggal']
        Harga = request.POST['Harga']
        Alamat = request.POST['Alamat']
        
        bookings = Bookings(
            wedding_id=wedding_id,
            Paket=Paket,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            No_HP=No_HP,
            Tanggal=Tanggal,
            Harga=Harga,
            Alamat=Alamat,
            Booking=False  # Set default is_approved value to False
        )
        bookings.save()

        messages.success(request, 'Your request has been submitted. We will get back to you shortly.')
        return redirect('dashboard')

    return render(request, 'inquiry.html')


def make_payment(request, inquiry_id):
    if request.method == 'POST':
        proof_file = request.FILES.get('proof_file')
        inquiry = Bookings.objects.get(id=inquiry_id)
        inquiry.proof_file = proof_file
        inquiry.save()
        messages.success(request, 'Proof of payment has been uploaded successfully.')
        return redirect('dashboard')

    inquiry = Bookings.objects.get(id=inquiry_id)

    context = {
        'inquiry': inquiry,
    }

    return render(request, 'make_payment.html', context)


def upload_proof(request, inquiry_id):
    if request.method == 'POST':
        proof_file = request.FILES.get('proof_file')
        inquiry = Bookings.objects.get(id=inquiry_id)
        inquiry.proof_file = proof_file
        inquiry.save()
        messages.success(request, 'Proof of payment has been uploaded successfully.')
        return redirect('dashboard')
    
    return render(request, 'upload_proof.html', {'inquiry_id': inquiry_id})


def bayar_di_tempat(request, inquiry_id):
    inquiry = Bookings.objects.get(id=inquiry_id)
    if not inquiry.Booking:  # Check if the inquiry is not already approved
        inquiry.Booking = False
        inquiry.keterangan = 'Bayar di Tempat'
        inquiry.save()
        messages.success(request, 'Payment will be made on-site. Thank you for your reservation.')
    else:
        messages.info(request, 'Payment method already set to "Bayar di Tempat".')

    return redirect('dashboard')


def validate_payment(request, inquiry_id):
    inquiry = Bookings.objects.get(id=inquiry_id)
    inquiry.Vadid = True
    inquiry.save()
    messages.success(request, 'Payment validation successful.')
    return redirect('dashboard')


def print_receipt(request, inquiry_id):
    inquiry = get_object_or_404(Bookings, id=inquiry_id)
    return render(request, 'print_receipt.html', {'inquiry': inquiry})

