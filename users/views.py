from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,  UserUpdateForm, ProfileRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created you can now log in ")
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = UserUpdateForm(request.POST, instance = request.user)
        i_form = ProfileRegisterForm(request.POST, request.FILES, instance = profile)
        if p_form.is_valid() and i_form.is_valid():
            p_form.save()
            i_form.save()
            messages.success(request, f"Your profile has been updated")
            return redirect('profile')
    else:
        p_form = UserUpdateForm( instance = request.user)
        i_form = ProfileRegisterForm( instance = request.user.profile)
    context = {
        'p_form':p_form,
        'i_form':i_form
    }

    return render(request, 'users/profile.html', context)