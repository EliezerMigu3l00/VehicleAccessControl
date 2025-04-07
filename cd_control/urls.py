from django.urls import path
from cd_control.views import EntryExitView, VehicleView, FirmView, ProductTypeView, VehicleTypeView, DriverView

urlpatterns = [
    path('entry-exit/', EntryExitView.as_view(), name='entry_exit'),
    path('vehicle/', VehicleView.as_view(), name='vehicle'),
    path('firm/', FirmView.as_view(), name='firm'),
    path('product-type/', ProductTypeView.as_view(), name='product_type'),
    path('vehicle-type/', VehicleTypeView.as_view(), name='vehicle_type'),
    path('driver/', DriverView.as_view(), name='driver'),
]