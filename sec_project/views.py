from django.shortcuts import render


def my_custom_error_view(request, exception):
    return render(request, 'error_view.html', status=404)

