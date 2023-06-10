from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect
from urllib.parse import quote_plus, urlencode
from profiles.models import Profile
from django.urls import reverse_lazy
from django.utils import timezone

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse_lazy("accounts:callback"))
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    userinfo = token.get('userinfo')

    email = userinfo['email']
    nickname = userinfo['nickname']
    existing_profile = Profile.objects.filter(email=email).first()
    if not existing_profile:
        profile = Profile(email=email, nickname=nickname, registration_time=timezone.now().date())
        profile.save()
    else:
        profile = existing_profile

    profile_id = profile.id

    userinfo = {'id': profile_id, **userinfo}
    token['userinfo'] = userinfo

    request.session["user"] = token['userinfo']

    return redirect('/profiles/home')


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )


def index(request):
    return render(request, "index.html")
