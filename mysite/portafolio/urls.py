from django.urls import path, include
from .views import Index, portfolio

urlpatterns = [
    path('portafolio', portfolio, name='portafolio')

]


