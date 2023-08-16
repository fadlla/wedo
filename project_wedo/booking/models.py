from django.db import models
from datetime import datetime


class Bookings(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    No_HP = models.CharField(max_length=20, blank=True)
    wedding_id = models.IntegerField()
    Paket = models.CharField(max_length=100)
    Tanggal = models.DateField()
    Alamat = models.CharField(max_length=100)
    proof_file = models.FileField(upload_to='proofs/', blank=True, null=True)
    proof_file_cash = models.ImageField(upload_to='proofs/', null=True, blank=True)
    Harga = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)
    keterangan = models.CharField(max_length=100, blank=True)
    Valid = models.BooleanField(default=False)
    Booking = models.BooleanField(default=False)

    def __str__(self):
        return self.Paket

    def full_name(self):
        return f"{self.Nama} {self.last_name}"

    def save(self, *args, **kwargs):
        if self.proof_file_cash:
            self.proof_file = None
        super().save(*args, **kwargs)


class Inquiry(models.Model):
    Paket = models.CharField(max_length=100)

    def __str__(self):
        return self.Paket