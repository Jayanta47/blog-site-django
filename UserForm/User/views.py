from django.shortcuts import render, redirect
from User.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def test_index(request):
    return render(request, 'User/test_index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'User/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'User/profile.html')
