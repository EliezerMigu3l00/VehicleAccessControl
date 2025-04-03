from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from cd_control.models import ProductType


class ProductTypeView(View):
    def get(self, request):
        product_types = ProductType.objects.all()
        context = {
            'product_types': product_types,
        }
        return render(request, 'cd_control/product_type.html', context)

    def post(self, request):
        name = request.POST.get('name')
        try:
            ProductType.objects.create(name=name)
            messages.success(request, "Tipo de produto criado com sucesso!")
            return redirect('product_type')
        except Exception as e:
            messages.error(request, f"Erro ao criar tipo de produto: {e}")
            return redirect('product_type')