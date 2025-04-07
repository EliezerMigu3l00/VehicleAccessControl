from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from cd_control.models import VehicleType


class VehicleTypeView(View):
    def get(self, request):
        vehicle_types = VehicleType.objects.all()
        context = {
            'vehicle_types': vehicle_types,
        }
        return render(request, 'cd_control/support_function.html', context)

    def post(self, request):
        name = request.POST.get('name')
        try:
            VehicleType.objects.create(name=name)
            messages.success(request, "Tipo de veículo criado com sucesso!")
            return redirect('vehicle_type')
        except Exception as e:
            messages.error(request, f"Erro ao criar tipo de veículo: {e}")
            return redirect('vehicle_type')