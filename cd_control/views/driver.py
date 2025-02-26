from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cd_control.models.driver import Driver


class DriverListView(ListView):
    model = Driver


class DriverCreateView(CreateView):
    model = Driver
    fields = ["name", "cpf", "rg", "cnh", "phone", "firm"]
    success_url = reverse_lazy("driver_list")


class DriverUpdateView(UpdateView):
    model = Driver
    fields = ["name", "cpf", "rg", "cnh", "phone", "firm"]
    success_url = reverse_lazy("driver_list")


class DriverDeleteView(DeleteView):
    model = Driver
    success_url = reverse_lazy("driver_list")
