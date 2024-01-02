# admin.py

from django.contrib import admin
from .models import ChatMessage, genaiSetting, Conversation


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id','start_date','active')
    list_filter = ('start_date',)
    search_fields = ('start_date',)





admin.site.register(Conversation, ConversationAdmin)
class ChatLogAdmin(admin.ModelAdmin):
  list_display = ('conversation','message', 'response', 'timestamp')
  list_filter = ('timestamp',)
  search_fields = ('message', 'response')

admin.site.register(ChatMessage, ChatLogAdmin)

class genaiSettingAdmin(admin.ModelAdmin):
  list_display = ('id','temperture', 'max_length', 'top_p', 'top_k')
  list_filter = ('temperture', 'max_length', 'top_p', 'top_k')
  search_fields = ('temperture', 'max_length', 'top_p', 'top_k')

admin.site.register(genaiSetting, genaiSettingAdmin)