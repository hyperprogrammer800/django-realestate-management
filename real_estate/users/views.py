from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, TenantUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def tenant(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        t_form = TenantUpdateForm(request.POST,
                                  request.FILES, 
                                  instance=request.user.tenant)
        if u_form.is_valid()  and t_form.is_valid():
            u_form.save()
            t_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('tenant')
    else:
        u_form = UserUpdateForm(instance=request.user)
        t_form = TenantUpdateForm(instance=request.user.tenant)
    context = {
        'u_form' : u_form,
        't_form' : t_form
    }
    return render(request, 'users/tenant.html', context)