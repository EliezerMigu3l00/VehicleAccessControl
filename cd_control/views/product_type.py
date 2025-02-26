from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cd_control.models.product_type import ProductType


class ProductTypeListView(ListView):
    model = ProductType


class ProductTypeCreateView(CreateView):
    model = ProductType
    fields = ["name"]
    success_url = reverse_lazy("product_type_list")


class ProductTypeUpdateView(UpdateView):
    model = ProductType
    fields = ["name"]
    success_url = reverse_lazy("product_type_list")


class ProductTypeDeleteView(DeleteView):
    model = ProductType
    success_url = reverse_lazy("product_type_list")
