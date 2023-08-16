from django.db import models
from django.contrib.auth.models import User

from wedding.models import Wedding

from django.db import models
from django.contrib.auth.models import User
from wedding.models import Wedding

class Order(models.Model):
    wedding_title = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.wedding_title)

    def get_order_details(self):
        return f"Order: {self.wedding_title} | Price: {self.price} | User: {self.user}"



class Approval(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

class Transaction(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    # tambahkan bidang lain yang diperlukan untuk transaksi
