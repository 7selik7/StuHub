from django.shortcuts import render
from profiles.models import Profile
from .models import Profile



from django.shortcuts import render

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
