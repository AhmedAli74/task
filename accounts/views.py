from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import SignupForm,ProfileForm,UserForm
from .models import Profile,User
from django.http import Http404

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('Home:Home')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form, })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('Home:Home')
        else:
            raise Http404("Page not found")
    return render(request,'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login')