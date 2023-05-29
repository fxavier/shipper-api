from rest_framework import serializers
from core.models import Service, Shipment, ShippingLabel, StatusUpdate, \
    Notification, Report


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'price')


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ('id', 'origin', 'destination', 'weight', 'dimensions',
                  'volume',
                  'service', 'phone_sender', 'name_sender', 'phone_receiver',
                  'name_receiver', 'created_by', 'created_at', 'modified_by')


class ShippingLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingLabel
        fields = ('id', 'shipment', 'barcode')


class StatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusUpdate
        fields = ('id', 'shipment', 'status', 'updated_at')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'shipment', 'recipient',
                  'notification_type', 'sent_at')


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'shipment', 'delivery_time', 'freight_cost')
