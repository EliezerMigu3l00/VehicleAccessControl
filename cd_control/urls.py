from django.urls import path
from cd_control.views import EntryExitView, VehicleView

urlpatterns = [
    path('entry-exit/', EntryExitView.as_view(), name='entry_exit'),
    path('vehicle/', VehicleView.as_view(), name='vehicle'),
]