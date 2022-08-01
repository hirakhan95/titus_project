from django.shortcuts import render


# Create your views here.

def example_view(request):
    # titus/templates/titus/example.html
    return render(request, 'titus/example.html')


def variable_view(request):
    my_var = {'first_name': 'ANNE',
              'last_name': 'FrAnk',
              'some_list': [1, 2, 3],
              'some_dict': {'inside_key': 'inside_value'},
              'user_logged_in': False}


    return render(request, 'titus/variable.html', context=my_var)
