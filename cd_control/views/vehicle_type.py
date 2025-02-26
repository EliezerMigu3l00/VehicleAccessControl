from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cd_control.models.vehicle_type import VehicleType


class VehicleTypeListView(ListView):
    model = VehicleType


class VehicleTypeCreateView(CreateView):
    model = VehicleType
    fields = ["name", "description"]
    success_url = reverse_lazy("vehicle_type_list")


class VehicleTypeUpdateView(UpdateView):
    model = VehicleType
    fields = ["name", "description"]
    success_url = reverse_lazy("vehicle_type_list")


class VehicleTypeDeleteView(DeleteView):
    model = VehicleType
    success_url = reverse_lazy("vehicle_type_list")
