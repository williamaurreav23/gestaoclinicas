from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.shortcuts import redirect


def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = UserCreationForm()
    return render(request, 'login.html', {
        'form': form
    })
