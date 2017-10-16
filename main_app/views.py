from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'treasure_name': 'Gold Nugget',
               'treasure_value': 1000.00}
    return render(request, 'index.html', context)
