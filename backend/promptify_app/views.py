from django.shortcuts import render
from rest_framework.response import Response

from promptify_app.models import Chat


def prompt_gpt(request):
    chat_id = request.data.get("chat_id")
    content = request.data.get("content")

    if not chat_id:
        return Response({"error": "Chat ID was not provided"}, status=400)

    if not content:
        return Response({"error": "There was no prompt passed"}, status=400)

    chat, created = Chat.object.get_or_create(id=chat_id)
