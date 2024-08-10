from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # Redirect to the greeting page with the name as a URL parameter
            return redirect('greet', name=name)
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})

def greet(request, name):
    return HttpResponse(f'Hi {name}')

