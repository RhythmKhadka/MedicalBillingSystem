from django.shortcuts import render
from .models import Purchase
from .models import Products
from django.http import HttpResponse
from .forms import AddPurchaseForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required (login_url = '/login/')
def purchase_update(request,id):
    purchase= Purchase.objects.get(pk=id)
    form = AddPurchaseForm(request.POST or None,instance=purchase)
    if form.is_valid():
        form.save()
        return redirect('purchase')
    context = {
    'form':form,
    }
    return render(request,'purchase_update.html',context)


def invoices(request):
    context={
    'products':Products.objects.all()
    }
    return render(request,'pos.html',context)
