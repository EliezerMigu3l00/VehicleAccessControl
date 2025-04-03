from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from cd_control.models import Firm


class FirmView(View):
    def get(self, request):
        name = Firm.objects.all()
        cnpj = Firm.objects.all()

        context = {
            'name': name,
            'cnpj': cnpj,
        }

        return render(request, 'cd_control/firm.html', context)

    def post(self, request):
        name = request.POST.get('name')
        cnpj = request.POST.get('cnpj')

        try:
            Firm.objects.create(
                name=name,
                cnpj=cnpj
            )
            messages.success(request, "Empresa criada com sucesso!")
            return redirect('firm')
        except Exception as e:
            messages.error(request, f"Erro ao criar empresa: {e}")
            return redirect('firm')