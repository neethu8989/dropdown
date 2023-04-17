from django.contrib import auth, messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, Branches


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Registered")
            return render(request, 'login.html')
    else:

        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def loginpage(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('formpage')
        else:
            messages.info(request, 'username or password incorrect')
            return render(request, 'login.html')

    return render(request, 'login.html')


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Application accepted", )
            return redirect('/')
    return render(request, 'formpage.html', {'form': form})


# def Userform(request):
#     form = PersonCreationForm()
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Successfully Registered", )
#             return redirect('/')
#     return render(request, 'formpage.html', {'form': form})


def load_cities(request):
    district_id = request.GET.get('district_id')
    branches = Branches.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown_list_options.html', {'branches': branches})

    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def logout(request):
    auth.logout(request)
    return redirect('/')
