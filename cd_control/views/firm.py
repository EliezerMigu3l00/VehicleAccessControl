from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cd_control.models.firm import Firm


class FirmListView(ListView):
    model = Firm


class FirmCreateView(CreateView):
    model = Firm
    fields = ["name", "cnpj"]
    success_url = reverse_lazy("firm_list")


class FirmUpdateView(UpdateView):
    model = Firm
    fields = ["name", "cnpj"]
    success_url = reverse_lazy("firm_list")


class FirmDeleteView(DeleteView):
    model = Firm
    success_url = reverse_lazy("firm_list")