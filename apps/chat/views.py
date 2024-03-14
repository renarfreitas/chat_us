from django.shortcuts import render
from .models import Message, Room


def index(request):
    messages = Message.objects.all()
    
    rooms = Room.objects.all()

    return render(request, 'chat/index.html', {
        'rooms': rooms,
        'messages': messages
    })