from django.shortcuts import render, redirect
from .models import Team
from wedding.models import Wedding
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from .models import Testimony
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    teams = Team.objects.all()
    Unggulan_Weddings = Wedding.objects.order_by('-created_date').filter(Unggulan=True)
    all_Weddings =  Wedding.objects.order_by('-created_date')
    durasi_acara = Wedding.objects.values_list('durasi_acara', flat=True).distinct()
    catering_search = Wedding.objects.values_list('catering_pack', flat=True).distinct()
    music_sound_search = Wedding.objects.values_list('music_sound', flat=True).distinct()
    wedding_organizer_search = Wedding.objects.values_list('wedding_organizer', flat=True).distinct()
    data = {
        'teams': teams,
        'Unggulan_Weddings': Unggulan_Weddings,
        'all_Weddings': all_Weddings,
        'durasi_acara': durasi_acara,
        'catering_search': catering_search,
        'music_sound_search' : music_sound_search,  
        'wedding_organizer_search' : wedding_organizer_search,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def testimony(request):
    return render(request, 'pages/testimony.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from WeddingDealer Website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'stevenazkamunira@gmail.com',
                [admin_email],
                fail_silently=True,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Testimony

@csrf_exempt
def save_testimonial(request):
    if request.method == 'POST':
        testimonial_text = request.POST.get('testimonial_text')

        # Simpan testimonial ke dalam model Testimony
        testimony = Testimony.objects.create(testimonial_text=testimonial_text)

        # Mengembalikan respons JSON yang sesuai
        return JsonResponse({'success': True, 'testimonial_id': testimony.id})
    else:
        return JsonResponse({'success': False})


from .models import Testimony

def testimony_view(request):
    testimonies = Testimony.objects.all()  # Mengambil semua data testimoni dari model

    context = {
        'testimonies': testimonies
    }
    return render(request, 'testimony.html', context)
