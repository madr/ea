from django.shortcuts import render


@requires_POST
def rvsp(request):
    # store to database

    # send confirmation email, if email was provided

    # send confirmation SMS, if phone was provided

    render(request, "ok")
