from django.shortcuts import render, redirect 
from .models import Destination
from .forms import DestinationForm

def index(request):
    # return render(request, 'index.html')
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.user = request.user  # Set the user to the logged-in user
            destination.save()
            return redirect('index')
    else:
        form = DestinationForm()
    return render(request, 'index.html', {'form': form})




def world_map(request):
    return render(request, 'world_map.html')
