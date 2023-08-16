from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib import admin
from .models import Bookings
from .models import Bookings


class BookingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'Paket', 'Tanggal', 'Harga', 'No_HP', 'Alamat','Booking', 'contact_button', 'view_proof','Valid',)
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'Alamat', 'Paket', 'No_HP')
    list_editable = ('Booking','Valid')
    list_per_page = 10
    


    def contact_button(self, obj):
        Tanggal = obj.Tanggal.strftime('%Y-%m-%d')
        message = "Helloo.. kami dari admin Wedding Organizers Pelangi ingin bertanya apakah benar memesan '{}' wedding pada tanggal {}?".format(obj.Paket, Tanggal)
        whatsapp_url = "https://api.whatsapp.com/send?phone=+6287860130305&text={}".format(message)
        return format_html('<a href="{}" class="button">Chat</a>', whatsapp_url)
    contact_button.short_description = 'Bookings'
        
    def approve_selected(self, request, queryset):
        queryset.update(Booking=True)

    def save_model(self, request, obj, form, change):
        if not obj.No_HP:
            obj.No_HP = request.user.No_HP
        super().save_model(request, obj, form, change)
        
    def view_proof(self, obj):
        if obj.proof_file:
            return format_html('<a href="{}" target="_blank">Lihat Bukti</a>', obj.proof_file.url)
        return "-"
    view_proof.short_description = 'Lihat Bukti'
    
    def validate_payment(self, request, queryset):
        queryset.update(Valid=True)
        self.message_user(request, "Selected payments have been validated.")
    validate_payment.short_description = "Validate Payment"

    actions = [validate_payment]

    def save_model(self, request, obj, form, change):
        if not change:  # Check if the object is being created or modified
            obj.Booking = False  # Set to False when created
            obj.keterangan = 'Tidak Valid'  # Set to 'Tidak Valid' when created

        super().save_model(request, obj, form, change)


admin.site.register(Bookings, BookingsAdmin)
