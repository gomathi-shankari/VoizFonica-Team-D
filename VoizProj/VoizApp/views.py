from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext

from VoizApp.models import prepaid,postpaid,dongle

# from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm, kycform, rechargeform, issueform, invoiceform


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                # login(request)
                return redirect('http://localhost:4200')
            elif username == "admin" and password == "root12345":
                return redirect('/adminhome')
            else:
                messages.info(request, 'username or password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logout(request):
    # logout(request)
    return redirect('/')


def index(request):
    return render(request, 'index.html')

def viewplans(request):
  records = prepaid.objects.all()
  res = postpaid.objects.all()
  result = dongle.objects.all()
  return render(request,'viewplans.html', {'records':records, 'res':res, 'result':result})

def offers(request):
    return render(request,'offers.html')


def home(request):
    context = {}
    form = kycform(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Our agent will reach you soon. Please keep your Aadhar Card / Driving License ready.')
        #return redirect('/index')
    context['form'] = form
    return render(request, 'home.html', context)


def recharge(request):
    context = {}
    form = rechargeform(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Recharge successful ')
        #return redirect('http://localhost:4200')
    context['form'] = form
    return render(request, 'recharge.html', context)


def issues(request):
  context = {}
  form = issueform(request.POST or None)
  if form.is_valid():
    form.save()
    messages.success(request, 'Issue submitted. Our agent will contact you soon')
    # return redirect('http://localhost:4200')
  context['form'] = form
  return render(request, 'issues.html', context)

def invoice(request):
  context = {}
  form = invoiceform(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('http://127.0.0.1:8000/invoice1/')
  context['form'] = form
  return render(request, 'invoice.html', context)


def invoice1(request):
  rec = recharging.objects.all()
  return render(request, 'invoice1.html', {'rec': rec})


def adminhome(request):
  records = prepaid.objects.all()
  res = postpaid.objects.all()
  result = dongle.objects.all()
  return render(request, 'adminhome.html', {'records': records, 'res': res, 'result': result})
