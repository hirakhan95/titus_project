from django.shortcuts import render

# Create your views here.


def example_view(request):
    # titus/templates/titus/example.html
    return render(request, 'titus/example.html')


def variable_view(request):
    return render(request, 'titus/variable.html')