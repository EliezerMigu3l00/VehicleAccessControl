from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from cd_control.models import Firm, Driver


class DriverView(View):
    def get(self, request):
        drivers = Driver.objects.all()
        firms = Firm.objects.all()

        context = {
            'drivers': drivers,
            'firms': firms,
        }

        return render(request, 'cd_control/driver.html', context)

    def post(self, request):
        name = request.POST.get('name')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        cnh = request.POST.get('cnh')
        phone = request.POST.get('phone')
        firm_id = request.POST.get('firm')

        try:
            Driver.objects.create(
                name=name,
                cpf=cpf,
                rg=rg,
                cnh=cnh,
                phone=phone,
                firm=Firm.objects.get(id=firm_id)
            )
            messages.success(request, "Motorista criado com sucesso!")
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar motorista: {e}")
        return redirect('driver')
