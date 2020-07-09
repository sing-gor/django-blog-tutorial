from django.shortcuts import render
from controllers.articles import models
# Create your views here.
from services.flash import Falsh



def home(request):
    falsh = Falsh

    context = {}
    queryset = models.Articles.objects.filter(data_status=0)

    context['falsh'] = falsh
    print(context)
    context['articles'] = queryset
    return render(request,'pages/home.html',context=context)
