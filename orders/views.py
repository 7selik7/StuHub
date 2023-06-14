from django.shortcuts import render, redirect
from django import forms
from .models import Order
from chat.models import Chat
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
    if order.dev_id != 0:
        return JsonResponse({'status': 'busy', 'message': 'Це замовлення вже виконується'})
    else:
        order.dev_id = request.session.get("user")['id']
        order.status = 1
        order.save()
        return JsonResponse({'status': 'free', 'message': 'Замовлення додано'})


def make_chat(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    user_id_1 = request.session.get("user")['id']
    user_id_2 = order.user_id
    if user_id_1 == user_id_2:
        return JsonResponse({'status': 'error', 'message': 'Неможливо створити чат'})
    user_ids = sorted([user_id_1, user_id_2])

    chat_name = f"chatu{user_ids[0]}u{user_ids[1]}"

    try:
        chat = Chat.objects.get(name=chat_name)
    except Chat.DoesNotExist:
        chat = Chat.objects.create(name=chat_name, user1_id=user_ids[0], user2_id=user_ids[1])
        return JsonResponse({'status': 'created', 'message': 'Чат створено'})
    return JsonResponse({'status': 'error', 'message': 'Чат вже створено'})


def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return JsonResponse({'status': 'done', 'message': 'Замовлення видалено'})
