from django.shortcuts import render, redirect, HttpResponse, reverse
from django.utils import timezone
from django.contrib import messages
from .forms import RegisterForm
import pytz
from .models import User
# Create your views here.
def timezone(request):
    request.session['django_timezone'] = request.POST['tz']
    print(request.POST['tz'])
    return HttpResponse(f"Timezone successfull set to {request.POST['tz']}")

def index(request):
    
    return render(request, 'index.html', { 'form': RegisterForm()})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if not User.objects.authenticate(email, password):
            messages.error(request, 'Invalid Credentials')
            return redirect('home:index')
        user = User.objects.get(email=email)
        request.session['user_id'] = user.id
        return redirect('posts:index')
    return redirect('home:index')

def logout(request):
    del request.session['user_id']
    return redirect('/')

def create(request):
    if request.method == 'POST':
        bound_form = RegisterForm(request.POST)
        if bound_form.is_valid():
            # create user?
            user = bound_form.save()
            request.session['user_id'] = user.id
            return redirect('/posts')
        else:
            return render(request, 'index.html', { 'form': bound_form })
