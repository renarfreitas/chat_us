from django.shortcuts import render
from .models import Message, Room
from django.views.generic.detail import DetailView

def index(request):
    
    rooms = Room.objects.all()

    return render(request, 'chat/index.html', {
        'rooms': rooms,

    })

class RoomDatailView(DetailView):
    model = Room
    template_name = 'chat/list-messages.html'

    def get_contexte_data(self, **kwargs):
        context = super().get_context__data(**kwargs)
        return context