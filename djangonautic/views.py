from django.http import HttpResponse


def homePage(request):
    return HttpResponse("HOMEPAGE")


def about(request):
    return HttpResponse("ABOUT")
