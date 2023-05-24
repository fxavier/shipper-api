from django.db import models
from users.models import User


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Shipment(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    dimensions = models.CharField(max_length=50)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    phone_sender = models.CharField(max_length=100)
    name_sender = models.CharField(max_length=100)
    phone_receiver = models.CharField(max_length=100)
    name_receiver = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        User, related_name="shipment", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_sender} - {self.name_receiver}"


class ShippingLabel(models.Model):
    shipment = models.OneToOneField(Shipment, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=100)

    def __str__(self):
        return self.shipment.name_sender


class StatusUpdate(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shipment.name_sender


class Notification(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    recipient = models.EmailField()
    notification_type = models.CharField(max_length=50)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shipment.name_sender


class Report(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    delivery_time = models.DurationField()
    freight_cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.shipment.name_sender
