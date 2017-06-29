from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
from django.template import loader
from django.http import HttpResponse
from .models import UserInfo

# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'infomgr/login.html')
    else:
        return HttpResponse('<h1>Whaduuuuup</h1>')

    # return render(request, 'infomgr/index.html', context={ "users": UserInfo.objects.filter(pk = 2) })
    #return HttpResponse('<h1>Ello There Matey</h1>')




def register(request):
    template_name = 'infomgr/registration.html'
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.set_password(password)

        user.save()
        user = authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('infomgr:index')

    context = {
        'form': form,
    }

    return render(request, template_name, context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'infomgr/index.html', context={'user': user})
            else:
                return render(request, 'infomgr/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'infomgr/login.html', {'error_message': 'Invalid login'})
    return render(request, 'infomgr/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'infomgr/login.html', context)