from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View, CreateView
from django.contrib.auth.models import User
from users.forms import NewUserForm
from .forms import PortfolioForm
from .models import Portfolio, ip
from django.contrib.auth.decorators import login_required
import datetime



class Index(View):
    print('Index')

class RegisterView(CreateView):
  template_name = "registration/register.html"
  form_class = NewUserForm

  def form_valid(self, form):
      form.save()
      return redirect('login')

@login_required
def portfolio(request):
    portfolio = Portfolio.objects.all()
    form = PortfolioForm()
    context = {'portfolio': portfolio, 'form':form}
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ipaddress = x_forwarded_for.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')
        get_ip= ip() 
        get_ip.ip_address= ipaddress
        get_ip.pub_date = datetime.date.today() 
        get_ip.save()
    return render(request, 'portafolio.html', context)

@login_required
def portafolio_import(request):
    portfolio = Portfolio.objects.all()
    context = {'portfolio': portfolio}
    form = PortfolioForm()
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('portafolio')
        else:
            form = PortfolioForm()
        return render(request, 'portafolio.html', context)