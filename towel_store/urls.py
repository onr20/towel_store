from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin

def index(request):
    return HttpResponse("Welcome to Towel Store")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('',index, name='index' ),


]


