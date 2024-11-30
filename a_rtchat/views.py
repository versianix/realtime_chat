from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name="public-chat")
    chat_messages = chat_group.chat_messages.all()[:30]
    return render(request, 'a_rtchat/chat.html', {'chat_messages': chat_messages})