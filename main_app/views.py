from django.shortcuts import render
from .models import models

# Create your views here.


def index(request):

    return render(request, 'index.html', {'locations': locations})


class Location(models.Model):
            name = models.CharField(max_length=100)
            predators = models.CharField(max_length=100)
            num_restaurants = models.IntegerField()
            img_url = models.CharField(max_length=100)


locations = [
    Location("Fool's Falls, CO", 'Flash Floods', 0,
             'http://courseware.codeschool.com/try_django/images/fools-falls.jpg'),
    Location("Curly's Creek, NM", 'Rattle Snakes', 2,
             'http://courseware.codeschool.com/try_django/images/curlys-creek.jpg'),
    Location('The Delicate Arch, UT', 'Scorpions', 0,
             'http://courseware.codeschool.com/try_django/images/delicate-arch.jpg')
]
