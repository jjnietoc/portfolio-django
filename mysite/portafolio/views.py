from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth.models import User
from users.forms import NewUserForm


class Index(View):
    print('Index')

class RegisterView(CreateView):
  template_name = "registration/register.html"
  form_class = NewUserForm

  def form_valid(self, form):
      form.save()
      return redirect('login')

def portfolio(request):
    user = User.objects.get()
    context = {
        'user': user
    }
    return render(request, 'portafolio.html', context)