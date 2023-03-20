
# Create your views here.
from django.shortcuts import render, redirect

from django.contrib.auth import login as auth_login


from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})