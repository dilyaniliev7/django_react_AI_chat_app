from openai import OpenAI
from django.shortcuts import render
from rest_framework.response import Response
from promptify_app.models import Chat


client = OpenAI()


def createChatTitle(user_message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "assistant", "content": "Give a short, descriptive title for this conversation in not more than 5 words."},
                {"role": "user", "content": user_message},
            ]
        )
        title = response.choices[0].message.content.strip()
    except Exception:
        title = user_message[:50]
    return title

def prompt_gpt(request):
    chat_id = request.data.get("chat_id")
    content = request.data.get("content")

    if not chat_id:
        return Response({"error": "Chat ID was not provided"}, status=400)

    if not content:
        return Response({"error": "There was no prompt passed"}, status=400)

    chat, created = Chat.object.get_or_create(id=chat_id)
    chat.title = createChatTitle(content)
    chat.save()
