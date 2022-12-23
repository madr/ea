from django.shortcuts import redirect, render
from .models import RVSPForm


def home(request):
    form = RVSPForm(request.POST) if request.method == "POST" else RVSPForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(success, success=True)
    return render(
        request,
        "invitation/home.html",
        context={
            "rvspform": form,
        },
    )
