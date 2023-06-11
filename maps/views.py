from django.shortcuts import render, redirect 
from .models import Destination
from .forms import DestinationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# @login_required
def index(request):
    # return render(request, 'index.html')
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            # destination = form.save(commit=False)
            if request.user.is_authenticated:
                form.instance.user = request.user  # Set the user to the logged-in user
                form.save()
                messages.success(request, 'New destination added')
                return redirect('index')
            else:
                messages.warning(request, 'Please login')
                return redirect('accounts/login')  # Redirect to the login page if the user is not authenticated
    else:
        form = DestinationForm()
    return render(request, 'index.html', {'form': form})
    
    # Display all destinations for the user
    destinations = Destination.objects.all()  # Retrieve all destinations from the database
    return render(request, 'index.html', {'destinations': destinations})



    # def index(request):
    # destinations = Destination.objects.filter(user=request.user).order_by('-visited_date')
    # form = DestinationForm()
    # return render(request, 'index.html', {'destinations': destinations, 'form': form})

@login_required
def add_destination(request):
    if request.method == 'POST':
        # user = request.user
        form = DestinationForm(request.POST)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.user = request.user # Assign the logged in user
            destination.save()
            messages.success(request, 'New destination added')
            form = DestinationForm()
            return redirect('index')
    else:
        form = DestinationForm()

    # return render(request, 'add_destination.html', {'form': form})
    context = {'form': form}
    return render(request, 'index.html', context)
    

def destination_list(request):
    destinations = Destination.objects.all()  # Retrieve all destinations from the database
    # context = {'destinations': destinations}
    # return render(request, 'destination_list.html', context)
    return render(request, 'index.html', {'destinations': destinations})


# def account_login(request):
#     return render(request, 'login.html')

# def logout_view(request):
#     logout(request)
#     return redirect('index')

# def world_map(request):
#     return render(request, 'world_map.html')
