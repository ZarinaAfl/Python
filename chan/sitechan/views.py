from datetime import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from sitechan.models import Message


def show_messages(request):
    messages = Message.objects.all()

    return render(request,
                  "chan/show_messages.html",
                  {"messages": messages}
    )

def reply(request, message_id):
    message = Message.objects.get(pk=message_id)
    return render(request,
                  "chan/reply.html",
                  {"message": message}
    )


def send(request):
    text_message = request.POST.get('message')

    m = Message(text=text_message)
    m.save()

    return redirect("/chan/")

def response(request, message_id):

    resp = request.POST.get('response')
    reply_to = Message.objects.get(pk=message_id)
    m = Message(text=resp, reply_to=reply_to)
    m.save()

    return redirect("/chan/")