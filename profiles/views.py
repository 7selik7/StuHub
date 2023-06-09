from .models import Profile
from orders.models import Order
from django.shortcuts import render
from profiles.models import Profile


def profile(request, profile_id):
    try:
        user_profile = Profile.objects.get(id=profile_id)
        context = {
            'profile': user_profile,
            'name': user_profile.nickname
        }
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        return render(request, 'profiles/profile_not_found.html')


def home(request):
    orders = Order.objects.all()
    return render(request, 'home.html', {'orders': orders})
