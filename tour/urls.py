from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addreview',views.addreview,name='addreview'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('booktour/<int:pk>',views.booktour,name='booktour'),
    path('booktourone/<int:pk>',views.booktourone,name='booktourone'),
    path('booktour/application',views.application,name='application'),
]
