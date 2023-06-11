from django.http import JsonResponse
from .models import Profile
from orders.models import Order
from django.shortcuts import render, redirect
from profiles.models import Profile
from django.shortcuts import get_object_or_404


def profile(request, profile_name):
    try:
        user_profile = Profile.objects.get(nickname=profile_name)
        context = {
            'profile': user_profile,
            'name': user_profile.nickname
        }
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        return render(request, 'profiles/profile_not_found.html')


def home(request):
    orders = Order.objects.all()

    userinfo = request.session.get("user") if request.session.get("user") else None
    if userinfo:
        name = userinfo.get("name")
        nickname = userinfo.get("nickname")
        picture = userinfo.get("picture")
        return render(request, 'home.html', {'orders': orders, 'name': name, 'nickname': nickname, 'picture': picture})
    else:
        return redirect('/')


def myorders(request):
    userinfo = request.session.get("user") if request.session.get("user") else None
    if userinfo:
        user_id = userinfo.get("id")
        name = userinfo.get("name")
        nickname = userinfo.get("nickname")
        picture = userinfo.get("picture")
        orders = Order.objects.filter(user_id=user_id)
        return render(request, 'myorders.html',
                      {'orders': orders, 'name': name, 'nickname': nickname, 'picture': picture})
    else:
        return redirect('/')


def mytasks(request):
    userinfo = request.session.get("user") if request.session.get("user") else None
    if userinfo:
        user_id = userinfo.get("id")
        name = userinfo.get("name")
        nickname = userinfo.get("nickname")
        picture = userinfo.get("picture")
        orders = Order.objects.filter(dev_id=user_id)
        return render(request, 'myorders.html',
                      {'orders': orders, 'name': name, 'nickname': nickname, 'picture': picture})
    else:
        return redirect('/')



