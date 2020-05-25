from django.shortcuts import render
from .models import *

# Create your views here.
def myview(request):
    queryset = ImagenesModel.objects.all()
    context = { "view_context" : queryset}
    return render(request, 'base.html' , context)