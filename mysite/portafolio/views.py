from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View, CreateView
from django.contrib.auth.models import User
from users.forms import NewUserForm
from .forms import PortfolioForm
from .models import Portfolio
from django.contrib.auth.decorators import login_required


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
    print(context)
    print(portfolio)
    return render(request, 'portafolio.html', context)

@login_required
def portafolio_import(request):
    portfolio = Portfolio.objects.all()
    context = {'portfolio': portfolio}
    form = PortfolioForm()
#    print(context)
 #  print(portfolio)
    if request.method == 'POST':
     #   print(request)
        form = PortfolioForm(request.POST, request.FILES)
        print(request.POST)
    #    print(form)
        if form.is_valid():
          #  print('ok!')
            form.save()
          #  print('saved')
            return HttpResponseRedirect('portafolio')
        else:
            form = PortfolioForm()
            #print('no entra')
            #print(form.errors.as_json())
        return render(request, 'portafolio.html', context)