# admin.py

from django.contrib import admin
from .models import ChatMessage

class ChatLogAdmin(admin.ModelAdmin):
  list_display = ('message', 'response', 'timestamp')
  list_filter = ('timestamp',)
  search_fields = ('message', 'response')

admin.site.register(ChatMessage, ChatLogAdmin)

