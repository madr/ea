from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import RVSPForm, InvitationResponse


def home(request):
    form = RVSPForm(request.POST) if request.method == "POST" else RVSPForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/?success=1")
    return render(
        request,
        "invitation/home.html",
        context={"rvspform": form, "success": "success" in request.GET},
    )


@login_required
def guests(request):
    guests = InvitationResponse.objects.filter(is_coming="yes")

    return HttpResponse(
        "\n".join(
            [
                ",".join(
                    [
                        "Namn",
                        "E-post",
                        "Telefon",
                        "Vuxna",
                        "Barn",
                        "Special",
                    ]
                )
            ]
            + [
                ",".join(
                    map(
                        str,
                        [
                            guest.name,
                            guest.email,
                            guest.phone,
                            guest.people_count,
                            guest.children_count,
                            guest.diet,
                        ],
                    )
                )
                for guest in guests
            ]
        ),
        content_type="text/csv",
    )
