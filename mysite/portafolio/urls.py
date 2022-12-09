from django.urls import path, include
from .views import portfolio, portafolio_import

urlpatterns = [
    path('portafolio', portfolio, name='portafolio'),
    path('portafolio_import', portafolio_import, name='portafolio_import')
] 


