from . import views
from django.urls import path
from .views import home

urlpatterns = [
    path('', views.home, name="home"),
    # path('login/',views.login_view, name='login'),
    # path('', views.login, name='login'),
    
]
#
