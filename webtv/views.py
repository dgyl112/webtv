from django.shortcuts import render


def bad_request(request, exception):
    return render(request, '400.html')


def permission_denied(request, exception):
    return render(request, '403.html')


def page_not_found(request, exception):
    return render(request, '404.html')


def error(request):
    return render(request, '500.html')
