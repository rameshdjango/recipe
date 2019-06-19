from django.shortcuts import render,reverse,get_object_or_404
from .models import Recipie
from django.http import HttpResponseRedirect

# Create your views here.

def recipie_list(request):
    recipie = Recipie.objects.all()
    return render(request,'recipie_app/recipielist.html',{'recipie_list':recipie})


def create_recipie(request):
    if request.method == 'GET':
        return render(request, 'dkrecipie/form create.html')
    elif request.method == 'POST':
        print (request.POST)
        Recipie.objects.create(recipie_name=request.POST.get('recipie_name'),
                               ingredients=request.POST.get('ingredients'),
                               process=request.POST.get('process'),
                               file_upload=request.FILES["file_field"])
        return HttpResponseRedirect(reverse('recipie_app:home'))


def detail(request, recipie_id):
    recipie = get_object_or_404(Recipie, pk=recipie_id)
    return render(request, 'recipie_app/detail.html', {'recipie': recipie})

