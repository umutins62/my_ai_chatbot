# admin.py

from django.contrib import admin
from .models import ChatMessage, genaiSetting

class ChatLogAdmin(admin.ModelAdmin):
  list_display = ('message', 'response', 'timestamp')
  list_filter = ('timestamp',)
  search_fields = ('message', 'response')

admin.site.register(ChatMessage, ChatLogAdmin)

class genaiSettingAdmin(admin.ModelAdmin):
  list_display = ('temperture', 'max_length', 'top_p', 'top_k', 'num_return_sequences', 'repetition_penalty', 'length_penalty', 'do_sample', 'early_stopping', 'num_beams')
  list_filter = ('temperture', 'max_length', 'top_p', 'top_k', 'num_return_sequences', 'repetition_penalty', 'length_penalty', 'do_sample', 'early_stopping', 'num_beams')
  search_fields = ('temperture', 'max_length', 'top_p', 'top_k', 'num_return_sequences', 'repetition_penalty', 'length_penalty', 'do_sample', 'early_stopping', 'num_beams')

admin.site.register(genaiSetting, genaiSettingAdmin)