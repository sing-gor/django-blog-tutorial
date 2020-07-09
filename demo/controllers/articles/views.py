from django.shortcuts import render, get_object_or_404
from controllers.articles import models
# Create your views here.
from services.flash import Falsh
# Create your views here.
def index(request):
    falsh = Falsh
    context = {}

    queryset = models.Articles.objects.filter(data_status=0)
    context['falsh'] = falsh
    print(context)
    context['articles'] = queryset
    return render(request,'pages/articles/index.html',context=context)

def show(request, id):
    falsh = Falsh
    context = {}

    queryone = get_object_or_404(models.Articles,id=id)
    context['falsh'] = falsh
    print(context)
    context['article'] = queryone
    return render(request,'pages/articles/show.html',context=context)
