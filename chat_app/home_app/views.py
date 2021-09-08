from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, 'home_app/index.html', {'username': request.user.username})


@login_required
def room(request, room_name):
    return render(request, 'home_app/chat_room.html', {
        'room_name': room_name,
        'username': request.user.username
    })