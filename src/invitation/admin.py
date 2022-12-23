from django.contrib import admin
from django.utils.translation import gettext as _
from .models import InvitationResponse

class InvitationResponseAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'ceremony', 'party', 'accommodation', 'acknowledged')
    ordering = ("-id", "-people_count")
    readonly_fields = (
        'is_coming',
        'is_partying',
        'phone',
        'email',
        'people_count',
        'children_count',
        'diet',
        'note',
        'consent',
        'verified'
    )

    @admin.display(description=_('Antal'))
    def count(self, obj):
        return "%s (%s)" % (
            obj.people_count + obj.children_count, 
            obj.children_count
        )

    @admin.display(description=_('Vigseln?'))
    def ceremony(self, obj):
        return "Ja!" if obj.is_coming == 'yes' else "Nej"

    @admin.display(description=_('Festen?'))
    def party(self, obj):
        return "Ja!" if obj.is_partying == 'yes' else "Nej"

    @admin.display(description=_('Campar?'))
    def accommodation(self, obj):
        return "-" if obj.camping == 'no' else obj.camping
    
    @admin.display(description=_('Kvittens skickad?'))
    def acknowledged(self, obj):
        return "Nej" if obj.verified == False else "Ja"


admin.site.register(InvitationResponse, InvitationResponseAdmin)