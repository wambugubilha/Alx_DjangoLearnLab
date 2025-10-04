# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms




def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Add more fields if needed

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'blog/profile.html', {'form': form})

