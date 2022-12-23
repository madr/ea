from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext as _

COMING_CHOICES = {
    "yes": "Ja!",
    "no": "Nej, jag/vi kan tyvärr inte komma",
}

PARTY_CHOICES = {
    "yes": "Ja!",
    "no": "Nej, jag/vi deltar endast vid ceremonin",
}

CAMPING_CHOICES = {
    "tent": "Ja, i tält",
    "rv": "Ja, i Husvagn",
    "no": "Nej, ingen campingplats",
}


class InvitationResponse(models.Model):
    name = models.CharField(_("Namn"), max_length=256)
    email = models.EmailField(_("E-postadress"), help_text="För bekräftelse/kvittens")
    phone = models.IntegerField(
        _("Telefonnummer"), help_text="För bekräftelse/kvittens"
    )
    is_coming = models.CharField(
        _("Kommer ni på bröllopet?"), max_length=4, choices=COMING_CHOICES.items()
    )
    is_partying = models.CharField(
        _("Stannar ni till middagen?"),
        max_length=4,
        choices=PARTY_CHOICES.items(),
        blank=True,
    )
    people_count = models.SmallIntegerField(_("Antal personer"), default=0)
    children_count = models.SmallIntegerField(_("Antal barn"), default=0)
    diet = models.TextField(_("Specialkost"), blank=True)
    camping = models.CharField(
        _("Campar ni vid Österå Bystuga?"),
        max_length=4,
        choices=CAMPING_CHOICES.items(),
    )
    note = models.TextField(_("Övrig kommentar"), blank=True)
    consent = models.BooleanField(
        _(
            "Ja, brudparet får spara mina uppgifter fram tills juli 2023 för att skicka information om bröllopet"
        )
    )
    verified = models.BooleanField(_("Kvittens skickad"), default=False)

    class Meta:
        verbose_name = _("Svar på inbjudan")
        verbose_name_plural = _("Svar på inbjudan")

    def __str__(self):
        return self.name


class RVSPForm(ModelForm):
    class Meta:
        model = InvitationResponse
        exclude = []
