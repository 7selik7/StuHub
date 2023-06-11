from django.shortcuts import render, redirect
from django import forms
from .models import Order
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['subject', 'description', 'deadline', 'price', 'type']


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_id = request.session["user"]['id']
            order.dev_id = 0
            order.status = 0
            order.save()
            return redirect('/profiles/home')
    else:
        form = OrderForm()

    context = {'form': form}
    return render(request, 'create_order.html', context)


def execute_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.dev_id = request.session.get("user")['id']
    order.save()

    return JsonResponse({'message': 'Заказ успешно выполнен'})
