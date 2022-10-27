from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('profile', views.profile, name='profile'),
    path('todays_market', views.todays_market, name='todays_market'),
    path('stock_rates', views.stock_rates, name='stock_rates'),
    path('reports', views.reports, name='reports'),
    path('main', views.main, name='main'),
]

