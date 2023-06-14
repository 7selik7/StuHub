from django.shortcuts import render, redirect
from chat.models import Chat
from .models import Message


def index(request):
    chats = Chat.objects.all()
    context = {
        'chats': chats
    }
    return render(request, "rooms.html", context)


def room(request, room_name):
    userinfo = request.session.get("user") if request.session.get("user") else None
    if userinfo:
        username = userinfo.get("nickname")

        messages = Message.objects.filter(chat=room_name).order_by("timestamp")

        return render(request, "room.html", {"room_name": room_name, "username": username, "messages": messages})
    else:
        return redirect('/')
