from rest_framework import viewsets
from core.models import (
    Service, Shipment, ShippingLabel, StatusUpdate,
    Notification, Report
)
from core.serializers import (ServiceSerializer, ShipmentSerializer,
                              ShippingLabelSerializer, StatusUpdateSerializer,
                              NotificationSerializer, ReportSerializer)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name', '')
        if name != '' and name is not None:
            qs = qs.filter(name=name)
        return qs  # This line is added so qs is returned in all cases.


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ShippingLabelViewSet(viewsets.ModelViewSet):
    queryset = ShippingLabel.objects.all()
    serializer_class = ShippingLabelSerializer


class StatusUpdateViewSet(viewsets.ModelViewSet):
    queryset = StatusUpdate.objects.all()
    serializer_class = StatusUpdateSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
