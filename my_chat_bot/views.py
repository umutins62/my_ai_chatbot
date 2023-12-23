from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render
from .utils import initials_image


# Create your views here.
def index(request):
    name = "Aras ÇELİK"
    img = initials_image(name)

    context = {
        "name": name,

    }
    return render(request, "index.html", context)
