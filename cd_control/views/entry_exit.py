from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from cd_control.models import EntryExit, Vehicle, Driver, Firm, ProductType


class EntryExitView(View):
    def get(self, request):
        entry_exits = EntryExit.objects.all()
        vehicles = Vehicle.objects.all()
        drivers = Driver.objects.all()
        firms = Firm.objects.all()
        products = ProductType.objects.all()

        entry_types = EntryExit.ENTRY_TYPES 

        context = {
            'entry_exits': entry_exits,
            'vehicles': vehicles,
            'drivers': drivers,
            'firms': firms,
            'products': products,
            'entry_types': entry_types,
        }

        return render(request, 'cd_control/entry_exit.html', context)

    def post(self, request):
        vehicle_id = request.POST.get('vehicle')
        driver_id = request.POST.get('driver')
        firm_id = request.POST.get('firm')
        entry_type = request.POST.get('entry_type')
        product_type_id = request.POST.get('product_type')
        pallets_quantity = request.POST.get('pallets_quantity')
        origin_route = request.POST.get('origin_route')
        authorized_by = request.POST.get('authorized_by')
        notes = request.POST.get('notes')

        product_type = ProductType.objects.get(id=product_type_id) if product_type_id else None
        pallets_quantity = int(pallets_quantity) if pallets_quantity else None

        try:
            EntryExit.objects.create(
                vehicle=Vehicle.objects.get(id=vehicle_id),
                driver=Driver.objects.get(id=driver_id),
                firm=Firm.objects.get(id=firm_id),
                entry_type=entry_type,
                product_type=product_type,
                pallets_quantity=pallets_quantity,
                origin_route=origin_route,
                authorized_by=authorized_by,
                notes=notes,
            )
            messages.success(request, "Registro criado com sucesso!")
            return redirect('entry_exit')
        except Exception as e:
            messages.error(request, f"Erro ao criar registro: {e}")
            return redirect('entry_exit')
