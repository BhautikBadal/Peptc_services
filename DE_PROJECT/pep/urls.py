from django.urls import path
from  . import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('homepage',views.homepage,name='homepage'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('email',views.email,name='email'),
    path('Delete/<int:id>',views.Delete,name='Delete'),
    path('reg_customer',views.reg_customer,name='reg_customer'),
    # path('reg_serviceprovider',views.reg_serviceprovider,name='reg_serviceprovider'),
    path('serviceRegistration',views.serviceRegistration,name='serviceRegistration'),
]