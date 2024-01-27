from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import houseform
from django.shortcuts import render, redirect, get_object_or_404
from .models import houses
from django.contrib.auth.decorators import login_required

list = []
form = houseform()
@login_required(login_url='/user/login')
def house_create(request):
    user = request.user
   # houses_list = houses.objects.all().values_list('name', flat=True)

    if request.method == 'POST':
        form = houseform(request.POST, request.FILES) #necessary if user wants to upload a picture
        if form.is_valid():
            instance = form.save(commit= False) #lets us make some changes on the form before saving it on database
            instance.clas = user
            instance.pic = request.POST.get('image',False)

             #  return redirect(////)
            if instance.title in list:
                house = houses.objects.filter(title = instance.title)
                house.delete()
            instance.save()
            return redirect('house:add')
    form = houseform()
    query = houses.objects.filter(clas = user)

    for house in query:
        list.append(house.title)

    return render(request, 'houses/addpage.html', {'form': form, 'houses_list':query})



def home_view(request):

        form = houseform()
        user = request.user
        query = houses.objects.all().values()

        return render(request, 'houses/homepage.html', {'form': form, 'houses_list': query})



def deletehouse(request, pk):
    item = houses.objects.get(id=pk)
    item.delete()
    return redirect('house:add')


def edithouse(request, pk):
    house_id = houses.objects.get(id=pk)
    form = houseform(instance=house_id)


    if request.method == "POST":
        form = houseform(request.POST, instance=house_id)
        if form.is_valid():
            form.save()
            return redirect('house:add')
    context = {'form': form}
    return render(request, 'houses/addpage.html', context)

def edandde(request):
    if 'edit' in request.POST:
        user = request.user
        students_list = houses.objects.all().values_list('name', flat=True)
        name = request.POST.get('tt')
        if name in list:
            house = houses.objects.filter(title=name,cls=user)
            form = houseform(instance=house)
            return redirect('houses:add')
        return redirect('houses:add')
    if 'delete' in request.POST:
        user = request.user
        if request.method == 'POST':
            name = request.POST.get('tt')
            house = houses.objects.filter(title=name, clas=user)
            if house.exists():
                house.delete()
            return redirect('houses:add')
        return redirect('houses:add')
    return redirect('houses:add')