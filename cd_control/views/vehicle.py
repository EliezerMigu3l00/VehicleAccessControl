from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from cd_control.models import Vehicle, VehicleType, Firm


class VehicleView(View):
    def get(self, request):
        vehicle_plate = Vehicle.objects.all()
        cart_plate = Vehicle.objects.all()
        vehicle_type = VehicleType.objects.all()
        firm = Firm.objects.all()

        context = {
            'vehicle_plate': vehicle_plate,
            'cart_plate': cart_plate,
            'vehicle_type': vehicle_type,
            'firm': firm,
        }

        return render(request, 'cd_control/vehicle.html', context)

    def post(self, request):
        vehicle_plate = request.POST.get('vehicle_plate')
        cart_plate = request.POST.get('cart_plate')
        vehicle_type_id = request.POST.get('vehicle_type')
        firm_id = request.POST.get('firm')

        try:
            Vehicle.objects.create(
                vehicle_plate=vehicle_plate,
                cart_plate=cart_plate,
                vehicle_type=VehicleType.objects.get(id=vehicle_type_id),
                firm=Firm.objects.get(id=firm_id)
            )
            messages.success(request, "Veículo criado com sucesso!")
            return redirect('vehicle')
        except Exception as e:
            messages.error(request, f"Erro ao criar veículo: {e}")
            return redirect('vehicle')