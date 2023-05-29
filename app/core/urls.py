from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ServiceViewSet, ShipmentViewSet, ShippingLabelViewSet, StatusUpdateViewSet, NotificationViewSet, ReportViewSet

router = DefaultRouter()
router.register('services', ServiceViewSet)
router.register('shipments', ShipmentViewSet)
router.register('shipping_labels', ShippingLabelViewSet)
router.register('status_updates', StatusUpdateViewSet)
router.register('notifications', NotificationViewSet)
router.register('reports', ReportViewSet)

app_name = 'core'

urlpatterns = [
    path('', include(router.urls)),
]
