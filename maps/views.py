from django.shortcuts import render, redirect 
from .models import Destination
from .forms import DestinationForm
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required


def index(request):
    # return render(request, 'index.html')
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            # destination = form.save(commit=False)
            form.instance.user = request.user  # Set the user to the logged-in user
            form.save()
            return redirect('index')
    else:
        form = DestinationForm()
    return render(request, 'index.html', {'form': form})



    # def index(request):
    # destinations = Destination.objects.filter(user=request.user).order_by('-visited_date')
    # form = DestinationForm()
    # return render(request, 'index.html', {'destinations': destinations, 'form': form})

# @login_required
def add_destination(request):
    if request.method == 'POST':
        user = request.user
        form = DestinationForm(request.POST)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.user = request.user
            destination.save()
    return redirect('destination_list')


def world_map(request):
    return render(request, 'world_map.html')
