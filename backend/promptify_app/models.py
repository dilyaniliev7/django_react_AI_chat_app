from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


MAX_TITLE_LENGTH = 255
MAX_CHAT_MESSAGE_ROLE_NAME_LENGTH = 15

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Chat(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=MAX_TITLE_LENGTH, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Session {self.id}"


class ChatMessage(models.Model):
    ROLES = (("assistant", "assistant"),
             ("user", "user")
             )

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=MAX_CHAT_MESSAGE_ROLE_NAME_LENGTH, choices=ROLES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role}: {self.content[:50]}"
