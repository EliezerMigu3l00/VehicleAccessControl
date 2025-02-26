from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cd_control.models.vehicle import Vehicle


class VehicleListView(ListView):
    model = Vehicle


class VehicleCreateView(CreateView):
    model = Vehicle
    fields = ["vehicle_plate", "cart_plate", "vehicle_type", "firm"]
    success_url = reverse_lazy("vehicle-list")


class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = ["vehicle_plate", "cart_plate", "vehicle_type", "firm"]
    success_url = reverse_lazy("vehicle-list")


class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy("vehicle-list")
