from django.urls import include, path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .landingPage import landingPage
urlpatterns = [
    path('', landingPage, name='landingPage'),
    path('register/',registration,name='registration'),
    path('login/',userLogin,name='login'),
    path('logout/',userLogout,name='user-logout'),
    path('user-dashboard/',clientDashboard,name='user-dashboard'),
    path('admin-dashboard/',adminDashboard,name='admin-dashboard'),
    path('order',order,name='order'),
    path('customer/<str:pk>/',customersDetails, name='customerDetail'),
    path('rest-view',viewRestaurant, name='rest-view'),
    path('delete_order/<str:pk>/',deleteOrder,name='delete-order'),
    path('dashboard/' ,redirectDash ,name='dashRedirec'),
    path('unauthor/',unauthor, name='unauthor')
    
]