from django.contrib import admin
from .models import InvitationResponse

class InvitationResponseAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_coming', 'is_partying')

admin.site.register(InvitationResponse, InvitationResponseAdmin)