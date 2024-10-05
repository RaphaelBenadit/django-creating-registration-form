from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')
def home(request):
    return render(request, 'home.html')

