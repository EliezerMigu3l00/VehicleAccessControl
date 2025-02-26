from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cd_control.models.entry_exit import EntryExit


class EntryExitListView(ListView):
    model = EntryExit


class EntryExitCreateView(CreateView):
    model = EntryExit
    fields = ["vehicle", "driver", "firm", "entry_type", "entry_datetime", "start_unload_datetime", "end_unload_datetime", "exit_datetime", "notes", "product_type", "pallets_quantity", "origin_route", "authorized_by"]
    success_url = reverse_lazy("entry_exit_list")


class EntryExitUpdateView(UpdateView):
    model = EntryExit
    fields = ["vehicle", "driver", "firm", "entry_type", "entry_datetime", "start_unload_datetime", "end_unload_datetime", "exit_datetime", "notes", "product_type", "pallets_quantity", "origin_route", "authorized_by"]
    success_url = reverse_lazy("entry_exit_list")


class EntryExitDeleteView(DeleteView):
    model = EntryExit
    success_url = reverse_lazy("entry_exit_list")
